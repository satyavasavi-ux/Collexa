import React, { useState } from 'react';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { Sparkles, Bot, Send, BrainCircuit, Activity, AlertTriangle, CheckCircle2, HelpCircle } from 'lucide-react';

const AIAssistantPortal = () => {
    const { user } = useAuth();
    const [query, setQuery] = useState('');
    const [conversation, setConversation] = useState([
        { role: 'assistant', text: 'Hello! I am your Collexa AI Campus Advisor. Ask me anything about academic regulations, exam schedules, attendance policies, fee structures, or library services!' }
    ]);
    const [loading, setLoading] = useState(false);

    // Predictor State
    const [attPct, setAttPct] = useState(88);
    const [internalMarks, setInternalMarks] = useState(85);
    const [assignmentScore, setAssignmentScore] = useState(90);
    const [gpa, setGpa] = useState(8.5);
    const [predictionResult, setPredictionResult] = useState(null);

    const handleSendQuery = async (e) => {
        e.preventDefault();
        if (!query.trim()) return;

        const userMsg = query;
        setConversation((prev) => [...prev, { role: 'user', text: userMsg }]);
        setQuery('');
        setLoading(true);

        try {
            const res = await api.post('/api/ai/assistant/query', { query: userMsg });
            setConversation((prev) => [...prev, { role: 'assistant', text: res.data.answer, sources: res.data.sources }]);
        } catch (err) {
            setConversation((prev) => [...prev, { role: 'assistant', text: 'Apologies, I encountered an error connecting to the knowledge base.' }]);
        } finally {
            setLoading(false);
        }
    };

    const handleRunPrediction = async () => {
        try {
            const res = await api.post('/api/ai/predict', {
                attendance_pct: parseFloat(attPct),
                internal_marks: parseFloat(internalMarks),
                assignment_scores: parseFloat(assignmentScore),
                gpa: parseFloat(gpa)
            });
            setPredictionResult(res.data);
        } catch (err) {
            alert('Failed to calculate academic forecast');
        }
    };

    return (
        <div className="space-y-8 animate-fade-in">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-indigo-950 via-purple-950 to-slate-950 p-8 rounded-3xl text-white shadow-xl border border-indigo-500/20">
                <div>
                    <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-purple-500/20 text-purple-300 text-xs font-bold uppercase tracking-wider mb-3">
                        <Sparkles className="h-3.5 w-3.5" />
                        <span>AI Academic Intelligence Suite</span>
                    </div>
                    <h1 className="text-3xl font-black tracking-tight">AI Campus Assistant & Predictive Analytics</h1>
                    <p className="text-slate-300 text-sm mt-1">Get instant answers on college regulations and forecast semester academic performance.</p>
                </div>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* AI Chat Window */}
                <div className="lg:col-span-2 bg-white rounded-3xl border border-slate-200 shadow-sm flex flex-col h-[560px] overflow-hidden">
                    <div className="p-4 border-b border-slate-100 bg-slate-50/50 flex items-center space-x-2">
                        <Bot className="h-5 w-5 text-indigo-600" />
                        <h3 className="text-xs font-black uppercase tracking-wider text-slate-800">Collexa AI Campus Q&A</h3>
                    </div>

                    <div className="flex-1 p-6 overflow-y-auto space-y-4 bg-slate-50/20">
                        {conversation.map((msg, i) => (
                            <div key={i} className={`flex flex-col ${msg.role === 'user' ? 'items-end' : 'items-start'}`}>
                                <div className={`p-4 rounded-2xl text-xs max-w-lg leading-relaxed ${
                                    msg.role === 'user' ? 'bg-indigo-600 text-white rounded-br-none shadow-sm' : 'bg-white text-slate-800 border border-slate-200 rounded-bl-none shadow-sm'
                                }`}>
                                    {msg.text}
                                    {msg.sources && msg.sources.length > 0 && (
                                        <div className="mt-2 pt-2 border-t border-slate-100 text-[10px] text-slate-400 font-bold">
                                            Source: {msg.sources.join(', ')}
                                        </div>
                                    )}
                                </div>
                            </div>
                        ))}
                        {loading && (
                            <div className="flex items-center space-x-2 text-xs text-slate-400 italic">
                                <Sparkles className="h-3.5 w-3.5 animate-spin text-indigo-500" />
                                <span>Collexa AI is thinking...</span>
                            </div>
                        )}
                    </div>

                    <form onSubmit={handleSendQuery} className="p-4 border-t border-slate-100 bg-white flex space-x-3">
                        <input
                            type="text"
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                            placeholder="Ask about attendance rule, exam hall ticket, library fine..."
                            className="flex-1 px-4 py-3 bg-slate-50 border border-slate-200 rounded-2xl text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                        />
                        <button type="submit" className="px-5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-2xl shadow-md transition-all">
                            <Send className="h-4 w-4" />
                        </button>
                    </form>
                </div>

                {/* Academic Performance Risk Predictor */}
                <div className="bg-white rounded-3xl p-6 border border-slate-200 shadow-sm space-y-6">
                    <div>
                        <div className="flex items-center space-x-2 text-purple-600 mb-1">
                            <BrainCircuit className="h-5 w-5" />
                            <h3 className="text-sm font-black uppercase tracking-wider">Academic Risk Predictor</h3>
                        </div>
                        <p className="text-xs text-slate-500">Heuristic ML performance model forecasting semester outcomes.</p>
                    </div>

                    <div className="space-y-4 text-xs">
                        <div>
                            <div className="flex justify-between font-bold mb-1">
                                <span>Attendance: {attPct}%</span>
                            </div>
                            <input
                                type="range"
                                min="40"
                                max="100"
                                value={attPct}
                                onChange={(e) => setAttPct(e.target.value)}
                                className="w-full accent-indigo-600"
                            />
                        </div>

                        <div>
                            <div className="flex justify-between font-bold mb-1">
                                <span>Internal Marks: {internalMarks}%</span>
                            </div>
                            <input
                                type="range"
                                min="30"
                                max="100"
                                value={internalMarks}
                                onChange={(e) => setInternalMarks(e.target.value)}
                                className="w-full accent-indigo-600"
                            />
                        </div>

                        <div>
                            <div className="flex justify-between font-bold mb-1">
                                <span>Assignment Avg: {assignmentScore}%</span>
                            </div>
                            <input
                                type="range"
                                min="40"
                                max="100"
                                value={assignmentScore}
                                onChange={(e) => setAssignmentScore(e.target.value)}
                                className="w-full accent-indigo-600"
                            />
                        </div>

                        <div>
                            <div className="flex justify-between font-bold mb-1">
                                <span>Current CGPA: {gpa}</span>
                            </div>
                            <input
                                type="range"
                                min="4.0"
                                max="10.0"
                                step="0.1"
                                value={gpa}
                                onChange={(e) => setGpa(e.target.value)}
                                className="w-full accent-indigo-600"
                            />
                        </div>

                        <button
                            onClick={handleRunPrediction}
                            className="w-full py-3 bg-purple-600 hover:bg-purple-700 text-white font-bold rounded-2xl shadow-md transition-all text-xs flex items-center justify-center space-x-2"
                        >
                            <Activity className="h-4 w-4" />
                            <span>Compute Predictive Forecast</span>
                        </button>
                    </div>

                    {predictionResult && (
                        <div className="p-4 rounded-2xl bg-indigo-50 border border-indigo-200 text-xs space-y-2">
                            <div className="flex justify-between items-center">
                                <span className="font-black text-indigo-900">Risk Assessment</span>
                                <span className="font-black px-2.5 py-0.5 rounded-full bg-indigo-600 text-white text-[10px]">{predictionResult.risk_level}</span>
                            </div>
                            <p className="text-slate-600 leading-relaxed">{predictionResult.recommendation}</p>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default AIAssistantPortal;
