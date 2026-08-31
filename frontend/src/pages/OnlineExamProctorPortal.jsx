import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { ShieldAlert, Video, AlertCircle, Clock, CheckCircle2, Award, ChevronRight, FileQuestion } from 'lucide-react';

const QUESTIONS = [
    { id: 1, q: "What is the worst-case time complexity of QuickSort?", options: ["O(n log n)", "O(n^2)", "O(n)", "O(log n)"], answer: 1 },
    { id: 2, q: "Which data structure is primarily used in Breadth-First Search (BFS)?", options: ["Stack", "Queue", "Priority Queue", "Binary Search Tree"], answer: 1 },
    { id: 3, q: "What does the 'I' in ACID properties of DBMS stand for?", options: ["Integrity", "Isolation", "Inheritance", "Index"], answer: 1 },
    { id: 4, q: "Which CPU scheduling algorithm can lead to starvation if not managed?", options: ["Round Robin", "Shortest Job First (SJF)", "FCFS", "First In First Out"], answer: 1 },
    { id: 5, q: "What is the primary objective of the Dijkstra algorithm?", options: ["Minimum Spanning Tree", "Single-Source Shortest Path", "Maximum Flow", "Topological Sort"], answer: 1 }
];

const OnlineExamProctorPortal = () => {
    const { user } = useAuth();
    const [answers, setAnswers] = useState({});
    const [timeLeft, setTimeLeft] = useState(1200); // 20 mins
    const [submitted, setSubmitted] = useState(false);
    const [score, setScore] = useState(null);
    const [events, setEvents] = useState([]);
    const [proctorStatus, setProctorStatus] = useState("Active - Camera & Audio Monitored");

    useEffect(() => {
        if (timeLeft > 0 && !submitted) {
            const timer = setInterval(() => setTimeLeft(t => t - 1), 1000);
            return () => clearInterval(timer);
        }
    }, [timeLeft, submitted]);

    // Track tab switch events for proctoring engine
    useEffect(() => {
        const handleVisibilityChange = () => {
            if (document.hidden && !submitted) {
                setEvents(prev => [...prev, { test_id: 101, type: "TAB_SWITCH", timestamp: new Date().toISOString() }]);
                setProctorStatus("⚠️ Warning: Tab switch / defocus detected!");
            }
        };
        document.addEventListener("visibilitychange", handleVisibilityChange);
        return () => document.removeEventListener("visibilitychange", handleVisibilityChange);
    }, [submitted]);

    const handleSubmitExam = async () => {
        setSubmitted(true);
        let correct = 0;
        QUESTIONS.forEach((q, idx) => {
            if (answers[idx] === q.answer) correct += 1;
        });
        setScore(correct);

        try {
            await api.post('/api/proctoring/evaluate', {
                test_id: 101,
                student_id: user?.id || 1,
                events: events
            });
        } catch (err) {
            console.error('Proctor evaluation error', err);
        }
    };

    const formatTime = (secs) => {
        const m = Math.floor(secs / 60);
        const s = secs % 60;
        return `${m}:${s < 10 ? '0' : ''}${s}`;
    };

    return (
        <div className="space-y-8 animate-fade-in">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-red-950 via-slate-900 to-slate-950 p-8 rounded-3xl text-white shadow-xl border border-red-500/20">
                <div>
                    <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-red-500/20 text-red-300 text-xs font-bold uppercase tracking-wider mb-3">
                        <Video className="h-3.5 w-3.5" />
                        <span>AI Video Proctoring & Integrity Engine</span>
                    </div>
                    <h1 className="text-3xl font-black tracking-tight">Autonomous Online Examination Terminal</h1>
                    <p className="text-slate-300 text-sm mt-1">CS501: Design & Analysis of Algorithms — Mid-Term Assessment</p>
                </div>
                <div className="flex items-center space-x-4">
                    <div className="bg-slate-900/80 px-5 py-3 rounded-2xl border border-slate-700 text-right">
                        <span className="text-[10px] text-slate-400 font-bold uppercase block">Time Remaining</span>
                        <span className="text-2xl font-mono font-black text-rose-400">{formatTime(timeLeft)}</span>
                    </div>
                </div>
            </div>

            {/* Proctor Alert */}
            <div className="p-4 rounded-2xl bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-bold flex items-center justify-between">
                <span className="flex items-center"><ShieldAlert className="h-4 w-4 mr-2" /> {proctorStatus}</span>
                <span>Infractions Logged: {events.length}</span>
            </div>

            {!submitted ? (
                <div className="space-y-6">
                    {QUESTIONS.map((q, idx) => (
                        <div key={q.id} className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-4">
                            <h3 className="text-sm font-bold text-slate-800 flex items-start">
                                <span className="p-1 px-2 rounded-lg bg-indigo-50 text-indigo-600 font-black text-xs mr-3">Q{idx + 1}</span>
                                <span>{q.q}</span>
                            </h3>
                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pl-8">
                                {q.options.map((opt, oIdx) => (
                                    <button
                                        key={oIdx}
                                        onClick={() => setAnswers(prev => ({ ...prev, [idx]: oIdx }))}
                                        className={`p-3.5 rounded-2xl border text-left text-xs font-medium transition-all ${
                                            answers[idx] === oIdx
                                                ? 'bg-indigo-600 text-white border-indigo-600 shadow-md font-bold'
                                                : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                                        }`}
                                    >
                                        {opt}
                                    </button>
                                ))}
                            </div>
                        </div>
                    ))}

                    <div className="flex justify-end pt-4">
                        <button
                            onClick={handleSubmitExam}
                            className="px-8 py-3.5 bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-black uppercase tracking-wider rounded-2xl shadow-xl transition-all"
                        >
                            Submit & Finalize Test
                        </button>
                    </div>
                </div>
            ) : (
                <div className="bg-white rounded-3xl p-10 border border-slate-200 shadow-xl text-center space-y-6 max-w-lg mx-auto">
                    <div className="h-16 w-16 bg-emerald-100 text-emerald-600 rounded-3xl flex items-center justify-center mx-auto shadow-inner">
                        <Award className="h-8 w-8" />
                    </div>
                    <div>
                        <h2 className="text-2xl font-black text-slate-800">Exam Submitted Successfully!</h2>
                        <p className="text-xs text-slate-500 mt-1">Your responses have been recorded and graded automatically.</p>
                    </div>
                    <div className="p-6 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span className="text-xs font-bold text-slate-400 uppercase">Score Obtained</span>
                        <div className="text-4xl font-black text-indigo-600">{score} / {QUESTIONS.length}</div>
                        <p className="text-xs font-bold text-emerald-600">{((score / QUESTIONS.length) * 100).toFixed(0)}% Accuracy</p>
                    </div>
                </div>
            )}
        </div>
    );
};

export default OnlineExamProctorPortal;
