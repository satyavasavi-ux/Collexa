import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { AlertCircle, Clock, CheckCircle2, Plus } from 'lucide-react';

const GrievanceRedressalPortal = () => {
    const [grievances, setGrievances] = useState([]);
    const [title, setTitle] = useState('');
    const [desc, setDesc] = useState('');
    const [category, setCategory] = useState('Academic');
    const [showForm, setShowForm] = useState(false);

    useEffect(() => {
        fetchGrievances();
    }, []);

    const fetchGrievances = async () => {
        try {
            const res = await api.get('/api/grievances/');
            setGrievances(res.data);
        } catch (err) {
            console.error('Failed to load grievances', err);
        }
    };

    const handleCreate = async (e) => {
        e.preventDefault();
        try {
            await api.post('/api/grievances/', {
                title: title,
                description: desc,
                category: category
            });
            setTitle('');
            setDesc('');
            setShowForm(false);
            fetchGrievances();
        } catch (err) {
            alert('Failed to submit ticket');
        }
    };

    return (
        <div className="space-y-8 animate-fade-in">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-slate-900 via-rose-950 to-slate-900 p-8 rounded-3xl text-white shadow-xl">
                <div>
                    <h1 className="text-3xl font-black tracking-tight">Student & Staff Grievance Redressal</h1>
                    <p className="text-slate-300 text-sm mt-1">Submit institutional issues with 48hr SLA resolution guarantee.</p>
                </div>
                <button
                    onClick={() => setShowForm(!showForm)}
                    className="px-5 py-2.5 bg-rose-600 hover:bg-rose-700 text-white text-xs font-bold rounded-xl shadow-md"
                >
                    {showForm ? 'Close Form' : 'Raise New Grievance'}
                </button>
            </div>

            {showForm && (
                <form onSubmit={handleCreate} className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4 max-w-xl mx-auto">
                    <h3 className="text-sm font-black text-slate-800">New Grievance Ticket</h3>
                    <input
                        type="text"
                        required
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                        placeholder="Brief summary of the issue..."
                        className="w-full p-3 bg-slate-50 border border-slate-200 rounded-xl text-xs"
                    />
                    <select
                        value={category}
                        onChange={(e) => setCategory(e.target.value)}
                        className="w-full p-3 bg-slate-50 border border-slate-200 rounded-xl text-xs font-bold"
                    >
                        <option value="Academic">Academic / Examination</option>
                        <option value="Hostel & Mess">Hostel & Mess</option>
                        <option value="Fee & Accounts">Fee & Accounts</option>
                        <option value="Infrastructure">Infrastructure & Labs</option>
                    </select>
                    <textarea
                        required
                        rows={3}
                        value={desc}
                        onChange={(e) => setDesc(e.target.value)}
                        placeholder="Provide details..."
                        className="w-full p-3 bg-slate-50 border border-slate-200 rounded-xl text-xs"
                    />
                    <button type="submit" className="w-full py-3 bg-rose-600 text-white font-bold text-xs rounded-xl">
                        Submit Grievance
                    </button>
                </form>
            )}

            <div className="space-y-4">
                {grievances.map(g => (
                    <div key={g.id} className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-2">
                        <div className="flex justify-between items-center">
                            <h4 className="text-sm font-bold text-slate-800">{g.title}</h4>
                            <span className="text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-800">{g.status}</span>
                        </div>
                        <p className="text-xs text-slate-600">{g.description}</p>
                        <p className="text-[10px] text-slate-400">Category: {g.category} • Submitted: {new Date(g.created_at).toLocaleDateString()}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default GrievanceRedressalPortal;
