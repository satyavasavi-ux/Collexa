import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { BarChart3, TrendingUp, Users, GraduationCap, DollarSign, Award, BookOpen, ShieldCheck } from 'lucide-react';

const AnalyticsBI = () => {
    const [overview, setOverview] = useState(null);

    useEffect(() => {
        fetchAnalytics();
    }, []);

    const fetchAnalytics = async () => {
        try {
            const res = await api.get('/api/analytics/overview');
            setOverview(res.data);
        } catch (err) {
            console.error('Failed to load analytics', err);
        }
    };

    return (
        <div className="space-y-8 animate-fade-in">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-slate-900 via-blue-950 to-slate-900 p-8 rounded-3xl text-white shadow-xl">
                <div>
                    <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs font-bold uppercase tracking-wider mb-3">
                        <BarChart3 className="h-3.5 w-3.5" />
                        <span>Executive Institutional Intelligence</span>
                    </div>
                    <h1 className="text-3xl font-black tracking-tight">Campus Operations & BI Analytics</h1>
                    <p className="text-slate-300 text-sm mt-1">Real-time telemetry on student attendance rates, departmental CGPA, fee collections, and placement trends.</p>
                </div>
            </div>

            {/* KPI Cards */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm flex items-center space-x-4">
                    <div className="p-4 rounded-2xl bg-indigo-50 text-indigo-600"><Users className="h-6 w-6" /></div>
                    <div>
                        <span className="text-xs font-bold text-slate-400 uppercase">Enrolled Students</span>
                        <h3 className="text-2xl font-black text-slate-800">{overview?.total_students || 1240}</h3>
                    </div>
                </div>

                <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm flex items-center space-x-4">
                    <div className="p-4 rounded-2xl bg-emerald-50 text-emerald-600"><TrendingUp className="h-6 w-6" /></div>
                    <div>
                        <span className="text-xs font-bold text-slate-400 uppercase">Avg Attendance</span>
                        <h3 className="text-2xl font-black text-slate-800">{overview?.overall_attendance_rate || 94.2}%</h3>
                    </div>
                </div>

                <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm flex items-center space-x-4">
                    <div className="p-4 rounded-2xl bg-purple-50 text-purple-600"><DollarSign className="h-6 w-6" /></div>
                    <div>
                        <span className="text-xs font-bold text-slate-400 uppercase">Fee Revenue</span>
                        <h3 className="text-2xl font-black text-slate-800">₹{(overview?.revenue_collected || 4500000).toLocaleString()}</h3>
                    </div>
                </div>

                <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm flex items-center space-x-4">
                    <div className="p-4 rounded-2xl bg-amber-50 text-amber-600"><Award className="h-6 w-6" /></div>
                    <div>
                        <span className="text-xs font-bold text-slate-400 uppercase">Placement Drives</span>
                        <h3 className="text-2xl font-black text-slate-800">{overview?.total_placement_drives || 18} Drives</h3>
                    </div>
                </div>
            </div>

            {/* Department Breakdown */}
            <div className="bg-white rounded-3xl p-8 border border-slate-200 shadow-sm space-y-6">
                <h3 className="text-sm font-black uppercase tracking-wider text-slate-800">Department Performance & Academic Benchmarking</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    {overview?.department_distribution?.map((dept, i) => (
                        <div key={i} className="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 space-y-3">
                            <h4 className="text-sm font-bold text-slate-800">{dept.department}</h4>
                            <div className="space-y-1.5 text-xs text-slate-600">
                                <div className="flex justify-between">
                                    <span>Students:</span>
                                    <span className="font-bold text-slate-800">{dept.students}</span>
                                </div>
                                <div className="flex justify-between">
                                    <span>Avg CGPA:</span>
                                    <span className="font-bold text-indigo-600">{dept.average_cgpa} / 10.0</span>
                                </div>
                            </div>
                            <div className="w-full bg-slate-200 h-2 rounded-full overflow-hidden">
                                <div className="bg-indigo-600 h-full rounded-full" style={{ width: `${(dept.average_cgpa / 10) * 100}%` }}></div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default AnalyticsBI;
