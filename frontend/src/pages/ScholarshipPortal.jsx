import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { Award, CheckCircle2, DollarSign, Calendar, ArrowUpRight } from 'lucide-react';

const ScholarshipPortal = () => {
    const [scholarships, setScholarships] = useState([]);

    useEffect(() => {
        api.get('/api/scholarships/').then(res => setScholarships(res.data)).catch(console.error);
    }, []);

    return (
        <div className="space-y-8 animate-fade-in">
            <div className="bg-gradient-to-r from-amber-950 via-slate-900 to-amber-900 p-8 rounded-3xl text-white shadow-xl">
                <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 text-xs font-bold uppercase tracking-wider mb-3">
                    <Award className="h-3.5 w-3.5" />
                    <span>Financial Aid & Grants</span>
                </div>
                <h1 className="text-3xl font-black tracking-tight">Merit Scholarships & Tuition Waivers</h1>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {scholarships.map(s => (
                    <div key={s.id} className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4 hover:shadow-md transition-all flex flex-col justify-between">
                        <div className="space-y-2">
                            <span className="text-sm font-black text-emerald-600">{s.amount}</span>
                            <h3 className="text-base font-black text-slate-800">{s.title}</h3>
                            <p className="text-xs text-slate-600 leading-relaxed">Criteria: {s.criteria}</p>
                            <p className="text-[10px] text-slate-400">Provider: {s.provider}</p>
                        </div>
                        <div className="pt-4 border-t border-slate-100 flex justify-between items-center">
                            <span className="text-[10px] text-rose-600 font-bold">Apply by: {s.deadline}</span>
                            <button className="px-4 py-2 bg-amber-500 hover:bg-amber-600 text-slate-950 text-xs font-black rounded-xl shadow-sm">
                                Apply
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ScholarshipPortal;
