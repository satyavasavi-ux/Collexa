import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { Briefcase, Building2, MapPin, DollarSign, Calendar, CheckCircle2, FileText, ArrowUpRight, Award, ShieldCheck } from 'lucide-react';

const PlacementPortal = () => {
    const { user } = useAuth();
    const [drives, setDrives] = useState([]);
    const [myApplications, setMyApplications] = useState([]);
    const [resumeUrl, setResumeUrl] = useState('');
    const [applyingDrive, setApplyingDrive] = useState(null);
    const [submitting, setSubmitting] = useState(false);
    const [msg, setMsg] = useState('');

    useEffect(() => {
        fetchPlacementData();
    }, []);

    const fetchPlacementData = async () => {
        try {
            const [drivesRes, appsRes] = await Promise.all([
                api.get('/api/placements/drives'),
                user?.role === 'STUDENT' ? api.get('/api/placements/my-applications') : Promise.resolve({ data: [] })
            ]);
            setDrives(drivesRes.data);
            setMyApplications(appsRes.data);
        } catch (err) {
            console.error('Failed to load placement data', err);
        }
    };

    const handleApply = async (e) => {
        e.preventDefault();
        if (!applyingDrive || submitting) return;
        setSubmitting(true);
        try {
            await api.post('/api/placements/apply', {
                drive_id: applyingDrive.id,
                student_id: user?.id,
                resume_url: resumeUrl?.trim() || 'https://drive.collexa.edu/resumes/my_resume.pdf'
            });
            setMsg(`Application successfully submitted to ${applyingDrive.company_name}!`);
            setApplyingDrive(null);
            setResumeUrl('');
            setTimeout(() => setMsg(''), 4000);
            fetchPlacementData();
        } catch (err) {
            alert(err.response?.data?.detail || 'Failed to submit application');
        } finally {
            setSubmitting(false);
        }
    };

    return (
        <div className="space-y-8 animate-fade-in">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-purple-900 via-indigo-900 to-slate-900 p-8 rounded-3xl text-white shadow-xl">
                <div>
                    <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-purple-500/20 text-purple-300 text-xs font-bold uppercase tracking-wider mb-3">
                        <Briefcase className="h-3.5 w-3.5" />
                        <span>Corporate Placement & Career Center</span>
                    </div>
                    <h1 className="text-3xl font-black tracking-tight">Campus Recruitment Drives & Careers</h1>
                    <p className="text-slate-300 text-sm mt-1">Explore Tier-1 software and engineering recruitment opportunities with top global employers.</p>
                </div>
            </div>

            {msg && (
                <div className="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-sm font-bold flex items-center shadow-sm">
                    <CheckCircle2 className="h-4 w-4 mr-2 text-emerald-600" />
                    {msg}
                </div>
            )}

            {/* Student Applications Status Tracker */}
            {user?.role === 'STUDENT' && myApplications.length > 0 && (
                <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                    <h3 className="text-xs font-black uppercase tracking-widest text-indigo-600">Your Active Job Applications ({myApplications.length})</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        {myApplications.map((app) => (
                            <div key={app.id} className="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                                <div className="flex justify-between items-center">
                                    <span className="text-xs font-bold text-slate-800">Drive #{app.drive_id}</span>
                                    <span className={`text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full ${
                                        app.status === 'Shortlisted' ? 'bg-emerald-100 text-emerald-700' : 'bg-blue-100 text-blue-700'
                                    }`}>
                                        {app.status}
                                    </span>
                                </div>
                                <p className="text-xs text-slate-600">{app.feedback || 'Application under screening by HR committee.'}</p>
                                <p className="text-[10px] text-slate-400">Applied: {new Date(app.applied_at).toLocaleDateString()}</p>
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Drives List */}
            <div className="space-y-4">
                <h2 className="text-xs font-black uppercase tracking-widest text-slate-500">Active Recruitment Drives</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {drives.map((d) => (
                        <div key={d.id} className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4 hover:shadow-md transition-all">
                            <div className="flex justify-between items-start">
                                <div>
                                    <div className="flex items-center space-x-2">
                                        <Building2 className="h-5 w-5 text-purple-600" />
                                        <h3 className="text-xl font-black text-slate-800">{d.company_name}</h3>
                                    </div>
                                    <h4 className="text-sm font-bold text-indigo-600 mt-1">{d.job_title}</h4>
                                </div>
                                <div className="text-right">
                                    <span className="text-lg font-black text-emerald-600">{d.salary_package}</span>
                                    <p className="text-[10px] text-slate-400">Fixed CTC</p>
                                </div>
                            </div>

                            <p className="text-xs text-slate-600 leading-relaxed">{d.job_description}</p>

                            <div className="grid grid-cols-2 gap-3 py-3 border-y border-slate-100 text-xs">
                                <div>
                                    <span className="text-slate-400 block text-[10px] uppercase font-bold">Eligibility</span>
                                    <span className="font-bold text-slate-700">CGPA ≥ {d.eligibility_cgpa}</span>
                                </div>
                                <div>
                                    <span className="text-slate-400 block text-[10px] uppercase font-bold">Location</span>
                                    <span className="font-bold text-slate-700 flex items-center"><MapPin className="h-3 w-3 mr-1 text-slate-400" /> {d.location}</span>
                                </div>
                                <div>
                                    <span className="text-slate-400 block text-[10px] uppercase font-bold">Drive Date</span>
                                    <span className="font-bold text-slate-700">{d.drive_date}</span>
                                </div>
                                <div>
                                    <span className="text-slate-400 block text-[10px] uppercase font-bold">Apply By</span>
                                    <span className="font-bold text-rose-600">{d.registration_deadline}</span>
                                </div>
                            </div>

                            {user?.role === 'STUDENT' && (
                                <button
                                    onClick={() => setApplyingDrive(d)}
                                    className="w-full py-3 bg-purple-600 hover:bg-purple-700 text-white text-xs font-bold rounded-xl shadow-md transition-all flex items-center justify-center space-x-2"
                                >
                                    <span>Apply for {d.company_name}</span>
                                    <ArrowUpRight className="h-4 w-4" />
                                </button>
                            )}
                        </div>
                    ))}
                </div>
            </div>

            {/* Application Modal */}
            {applyingDrive && (
                <div className="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 z-50 animate-fade-in">
                    <div className="bg-white rounded-3xl max-w-lg w-full p-8 shadow-2xl space-y-6">
                        <div className="flex justify-between items-center">
                            <div>
                                <span className="text-xs font-bold text-purple-600 uppercase">Application Submission</span>
                                <h3 className="text-xl font-black text-slate-800">{applyingDrive.company_name} - {applyingDrive.job_title}</h3>
                            </div>
                            <button onClick={() => setApplyingDrive(null)} className="text-slate-400 hover:text-slate-600 text-sm font-bold">✕</button>
                        </div>

                        <form onSubmit={handleApply} className="space-y-4">
                            <div>
                                <label className="block text-xs font-bold text-slate-700 mb-1">Resume / Portfolio Cloud URL</label>
                                <input
                                    type="url"
                                    required
                                    value={resumeUrl}
                                    onChange={(e) => setResumeUrl(e.target.value)}
                                    placeholder="https://drive.google.com/your-cv.pdf"
                                    className="w-full p-3 bg-slate-50 border border-slate-300 rounded-xl text-xs text-slate-800 focus:ring-2 focus:ring-purple-500 focus:outline-none"
                                />
                            </div>
                            <div className="p-4 rounded-xl bg-purple-50 border border-purple-200 text-purple-900 text-xs space-y-1">
                                <p className="font-bold">Eligibility Verification:</p>
                                <p>• Minimum CGPA Required: {applyingDrive.eligibility_cgpa}</p>
                                <p>• Departments: {applyingDrive.eligible_departments}</p>
                            </div>
                            <div className="flex space-x-3">
                                <button
                                    type="button"
                                    onClick={() => setApplyingDrive(null)}
                                    className="w-1/2 py-3 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold rounded-xl"
                                >
                                    Cancel
                                </button>
                                <button
                                    type="submit"
                                    disabled={submitting}
                                    className="w-1/2 py-3 bg-purple-600 hover:bg-purple-700 disabled:opacity-50 text-white text-xs font-bold rounded-xl shadow-md transition-all"
                                >
                                    {submitting ? 'Submitting...' : 'Submit Application'}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            )}
        </div>
    );
};

export default PlacementPortal;
