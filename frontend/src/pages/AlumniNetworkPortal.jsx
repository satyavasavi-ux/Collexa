import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { Users, Briefcase, MapPin, CheckCircle2, MessageSquare } from 'lucide-react';

const AlumniNetworkPortal = () => {
    const [alumni, setAlumni] = useState([]);

    useEffect(() => {
        api.get('/api/alumni/directory').then(res => setAlumni(res.data)).catch(console.error);
    }, []);

    return (
        <div className="space-y-8 animate-fade-in">
            <div className="bg-gradient-to-r from-blue-950 via-slate-900 to-indigo-950 p-8 rounded-3xl text-white shadow-xl">
                <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs font-bold uppercase tracking-wider mb-3">
                    <Users className="h-3.5 w-3.5" />
                    <span>Global Alumni Association</span>
                </div>
                <h1 className="text-3xl font-black tracking-tight">Collexa Alumni & Mentorship Network</h1>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                {alumni.map((alm, idx) => (
                    <div key={idx} className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4 hover:shadow-md transition-all">
                        <div className="h-12 w-12 rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 text-white flex items-center justify-center font-black text-lg shadow-md">
                            {alm.name[0]}
                        </div>
                        <div>
                            <h3 className="text-base font-black text-slate-800">{alm.name}</h3>
                            <p className="text-xs font-bold text-indigo-600">{alm.designation} at {alm.company}</p>
                            <p className="text-[10px] text-slate-400 mt-1">{alm.batch} • {alm.location}</p>
                        </div>
                        <div className="pt-3 border-t border-slate-100 flex justify-between items-center text-xs">
                            <span className={alm.mentorship_open ? "text-emerald-600 font-bold" : "text-slate-400"}>
                                {alm.mentorship_open ? "● Mentoring Open" : "Unavailable"}
                            </span>
                            <button className="px-3 py-1.5 bg-indigo-50 text-indigo-600 font-bold rounded-xl hover:bg-indigo-100">
                                Connect
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default AlumniNetworkPortal;
