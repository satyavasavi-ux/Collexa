import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { BookOpen, FileText, CheckCircle2, Clock, Upload, AlertCircle, Award, ChevronRight, Plus, ExternalLink, Calendar } from 'lucide-react';

const CourseLMSPortal = () => {
    const { user } = useAuth();
    const [subjects, setSubjects] = useState([]);
    const [selectedSubject, setSelectedSubject] = useState(null);
    const [modules, setModules] = useState([]);
    const [assignments, setAssignments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [activeTab, setActiveTab] = useState('modules');
    const [submissionText, setSubmissionText] = useState('');
    const [fileUrl, setFileUrl] = useState('');
    const [selectedAssignment, setSelectedAssignment] = useState(null);
    const [submitSuccess, setSubmitSuccess] = useState('');

    useEffect(() => {
        fetchSubjects();
    }, []);

    const fetchSubjects = async () => {
        setLoading(true);
        try {
            const res = await api.get('/api/courses/subjects');
            setSubjects(res.data);
            if (res.data.length > 0) {
                handleSelectSubject(res.data[0]);
            }
        } catch (err) {
            console.error('Failed to fetch subjects', err);
        } finally {
            setLoading(false);
        }
    };

    const handleSelectSubject = async (subject) => {
        setSelectedSubject(subject);
        try {
            const [modRes, assignRes] = await Promise.all([
                api.get(`/api/courses/subjects/${subject.id}/modules`),
                api.get(`/api/courses/assignments?subject_id=${subject.id}`)
            ]);
            setModules(modRes.data);
            setAssignments(assignRes.data);
        } catch (err) {
            console.error('Failed to fetch subject details', err);
        }
    };

    const handleAssignmentSubmit = async (e) => {
        e.preventDefault();
        if (!selectedAssignment) return;
        try {
            await api.post(`/api/courses/assignments/${selectedAssignment.id}/submit`, {
                assignment_id: selectedAssignment.id,
                student_id: user?.id,
                submission_text: submissionText,
                file_url: fileUrl || 'https://drive.collexa.edu/submissions/sample_assignment.pdf'
            });
            setSubmitSuccess('Assignment submitted successfully!');
            setSubmissionText('');
            setFileUrl('');
            setTimeout(() => setSubmitSuccess(''), 4000);
            handleSelectSubject(selectedSubject);
        } catch (err) {
            alert('Failed to submit assignment');
        }
    };

    return (
        <div className="space-y-8 animate-fade-in">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 p-8 rounded-3xl text-white shadow-xl">
                <div>
                    <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs font-bold uppercase tracking-wider mb-3">
                        <BookOpen className="h-3.5 w-3.5" />
                        <span>Academic Learning Management System</span>
                    </div>
                    <h1 className="text-3xl font-black tracking-tight">Course LMS & Syllabus Portal</h1>
                    <p className="text-slate-300 text-sm mt-1">Access lecture notes, module materials, and submit coursework assignments online.</p>
                </div>
            </div>

            {/* Main Content Layout */}
            <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
                {/* Subject Selector Sidebar */}
                <div className="lg:col-span-1 space-y-3">
                    <h2 className="text-xs font-black uppercase tracking-widest text-slate-500 px-2">Enrolled Courses</h2>
                    <div className="space-y-2">
                        {subjects.map((subj) => (
                            <button
                                key={subj.id}
                                onClick={() => handleSelectSubject(subj)}
                                className={`w-full text-left p-4 rounded-2xl border transition-all duration-200 ${
                                    selectedSubject?.id === subj.id
                                        ? 'bg-indigo-600 text-white border-indigo-500 shadow-lg shadow-indigo-600/30'
                                        : 'bg-white text-slate-700 border-slate-200 hover:border-indigo-300 hover:bg-slate-50'
                                }`}
                            >
                                <div className="flex items-center justify-between">
                                    <span className="text-xs font-black uppercase tracking-wider opacity-80">{subj.code}</span>
                                    <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-black/10">{subj.credits} Credits</span>
                                </div>
                                <h3 className="text-sm font-bold mt-1 line-clamp-1">{subj.name}</h3>
                                <p className="text-xs opacity-70 mt-1">{subj.department} • Sem {subj.semester}</p>
                            </button>
                        ))}
                    </div>
                </div>

                {/* Main Course Details */}
                <div className="lg:col-span-3 space-y-6">
                    {selectedSubject && (
                        <div className="bg-white rounded-3xl p-8 border border-slate-200 shadow-sm">
                            <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-slate-100 gap-4">
                                <div>
                                    <span className="text-xs font-bold text-indigo-600 uppercase tracking-wider">{selectedSubject.code}</span>
                                    <h2 className="text-2xl font-black text-slate-800">{selectedSubject.name}</h2>
                                    <p className="text-sm text-slate-500 mt-1">4 Hours/Week • {selectedSubject.credits} Credits • Semester {selectedSubject.semester}</p>
                                </div>
                                <div className="flex space-x-2">
                                    <button
                                        onClick={() => setActiveTab('modules')}
                                        className={`px-5 py-2.5 rounded-xl text-xs font-bold transition-all ${
                                            activeTab === 'modules'
                                                ? 'bg-indigo-600 text-white shadow-md'
                                                : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                                        }`}
                                    >
                                        Modules & Notes
                                    </button>
                                    <button
                                        onClick={() => setActiveTab('assignments')}
                                        className={`px-5 py-2.5 rounded-xl text-xs font-bold transition-all ${
                                            activeTab === 'assignments'
                                                ? 'bg-indigo-600 text-white shadow-md'
                                                : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                                        }`}
                                    >
                                        Assignments ({assignments.length})
                                    </button>
                                </div>
                            </div>

                            {/* Tab 1: Modules */}
                            {activeTab === 'modules' && (
                                <div className="mt-6 space-y-4">
                                    {modules.length === 0 ? (
                                        <div className="text-center py-12 text-slate-400 bg-slate-50 rounded-2xl border border-dashed border-slate-200">
                                            <BookOpen className="h-10 w-10 mx-auto mb-2 opacity-50" />
                                            <p className="font-semibold text-sm">Course modules & syllabus units will appear here.</p>
                                        </div>
                                    ) : (
                                        modules.map((mod) => (
                                            <div key={mod.id} className="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 hover:bg-slate-100/60 transition-all">
                                                <div className="flex items-center justify-between">
                                                    <span className="text-xs font-black uppercase tracking-wider text-indigo-600">Module {mod.module_number}</span>
                                                    <a href={mod.content_url || '#'} className="inline-flex items-center text-xs font-bold text-indigo-600 hover:underline">
                                                        <span>View Notes</span>
                                                        <ExternalLink className="h-3.5 w-3.5 ml-1" />
                                                    </a>
                                                </div>
                                                <h4 className="text-base font-bold text-slate-800 mt-1">{mod.title}</h4>
                                                <p className="text-xs text-slate-600 mt-2 leading-relaxed">{mod.description || 'Core theoretical concepts, algorithms, and practical application examples.'}</p>
                                            </div>
                                        ))
                                    )}
                                </div>
                            )}

                            {/* Tab 2: Assignments */}
                            {activeTab === 'assignments' && (
                                <div className="mt-6 space-y-6">
                                    {submitSuccess && (
                                        <div className="p-4 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-700 text-sm font-bold flex items-center">
                                            <CheckCircle2 className="h-4 w-4 mr-2" />
                                            {submitSuccess}
                                        </div>
                                    )}

                                    {assignments.length === 0 ? (
                                        <div className="text-center py-12 text-slate-400 bg-slate-50 rounded-2xl border border-dashed border-slate-200">
                                            <FileText className="h-10 w-10 mx-auto mb-2 opacity-50" />
                                            <p className="font-semibold text-sm">No assignments posted for this course yet.</p>
                                        </div>
                                    ) : (
                                        assignments.map((asgn) => (
                                            <div key={asgn.id} className="p-6 rounded-2xl bg-slate-50 border border-slate-200/80 space-y-4">
                                                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                                                    <div>
                                                        <h4 className="text-base font-bold text-slate-800">{asgn.title}</h4>
                                                        <div className="flex items-center space-x-3 text-xs text-slate-500 mt-1">
                                                            <span className="flex items-center"><Calendar className="h-3.5 w-3.5 mr-1" /> Due: {new Date(asgn.due_date).toLocaleDateString()}</span>
                                                            <span>•</span>
                                                            <span className="font-bold text-indigo-600">Max Points: {asgn.max_points}</span>
                                                        </div>
                                                    </div>
                                                    {user?.role === 'STUDENT' && (
                                                        <button
                                                            onClick={() => setSelectedAssignment(asgn)}
                                                            className="px-4 py-2 bg-indigo-600 text-white text-xs font-bold rounded-xl hover:bg-indigo-700 shadow-sm"
                                                        >
                                                            Submit Work
                                                        </button>
                                                    )}
                                                </div>
                                                <p className="text-xs text-slate-600 leading-relaxed">{asgn.description}</p>
                                            </div>
                                        ))
                                    )}

                                    {/* Submission Modal Form */}
                                    {selectedAssignment && (
                                        <div className="mt-6 p-6 rounded-2xl bg-indigo-50/50 border border-indigo-200 space-y-4">
                                            <div className="flex items-center justify-between">
                                                <h4 className="text-sm font-black text-indigo-900">Submit: {selectedAssignment.title}</h4>
                                                <button onClick={() => setSelectedAssignment(null)} className="text-xs font-bold text-slate-400 hover:text-slate-600">Cancel</button>
                                            </div>
                                            <form onSubmit={handleAssignmentSubmit} className="space-y-4">
                                                <div>
                                                    <label className="block text-xs font-bold text-slate-700 mb-1">Written Answer / Solution Notes</label>
                                                    <textarea
                                                        required
                                                        rows={3}
                                                        value={submissionText}
                                                        onChange={(e) => setSubmissionText(e.target.value)}
                                                        placeholder="Provide explanation of your methodology and answers..."
                                                        className="w-full p-3 bg-white border border-slate-300 rounded-xl text-xs text-slate-800 focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                                                    />
                                                </div>
                                                <div>
                                                    <label className="block text-xs font-bold text-slate-700 mb-1">Attachment URL / Drive Link (Optional)</label>
                                                    <input
                                                        type="url"
                                                        value={fileUrl}
                                                        onChange={(e) => setFileUrl(e.target.value)}
                                                        placeholder="https://drive.google.com/your-submission.pdf"
                                                        className="w-full p-3 bg-white border border-slate-300 rounded-xl text-xs text-slate-800 focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                                                    />
                                                </div>
                                                <button
                                                    type="submit"
                                                    className="px-6 py-2.5 bg-indigo-600 text-white text-xs font-bold rounded-xl hover:bg-indigo-700 shadow-md"
                                                >
                                                    Confirm & Submit Assignment
                                                </button>
                                            </form>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default CourseLMSPortal;
