import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { Calendar, Clock, BookOpen, User, CheckCircle2, AlertCircle } from 'lucide-react';

const DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
const SLOTS = [1, 2, 3, 4, 5, 6];

const TimetableSchedulerPortal = () => {
    const [entries, setEntries] = useState([]);
    const [department, setDepartment] = useState("Computer Science");
    const [semester, setSemester] = useState(5);

    useEffect(() => {
        fetchSchedule();
    }, [department, semester]);

    const fetchSchedule = async () => {
        try {
            const res = await api.get(`/api/timetable/entries?department=${department}&semester=${semester}`);
            setEntries(res.data);
        } catch (err) {
            console.error('Failed to load schedule', err);
        }
    };

    const getEntry = (day, slot) => {
        return entries.find(e => e.day_of_week === day && e.hour_slot === slot);
    };

    return (
        <div className="space-y-8 animate-fade-in">
            <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 p-8 rounded-3xl text-white shadow-xl flex justify-between items-center">
                <div>
                    <h1 className="text-3xl font-black tracking-tight">Institutional Timetable Matrix</h1>
                    <p className="text-slate-300 text-sm mt-1">Real-time scheduling grid with faculty and room allocations.</p>
                </div>
                <div className="flex space-x-3 text-xs">
                    <select
                        value={department}
                        onChange={(e) => setDepartment(e.target.value)}
                        className="bg-slate-800 border border-slate-700 text-white font-bold p-2.5 rounded-xl"
                    >
                        <option value="Computer Science">Computer Science</option>
                        <option value="Electronics & Comm">Electronics & Comm</option>
                        <option value="Information Technology">Information Technology</option>
                    </select>
                </div>
            </div>

            {/* Matrix Table */}
            <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm overflow-x-auto">
                <table className="w-full text-xs text-left">
                    <thead>
                        <tr className="border-b border-slate-100 text-[10px] uppercase font-black text-slate-400">
                            <th className="py-3 px-4">Day / Slot</th>
                            {SLOTS.map(s => <th key={s} className="py-3 px-4">Period {s} (Hour {s})</th>)}
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100">
                        {DAYS.map(day => (
                            <tr key={day} className="hover:bg-slate-50/50">
                                <td className="py-4 px-4 font-black text-slate-800">{day}</td>
                                {SLOTS.map(slot => {
                                    const entry = getEntry(day, slot);
                                    return (
                                        <td key={slot} className="py-3 px-4">
                                            {entry ? (
                                                <div className="p-3 rounded-2xl bg-indigo-50 border border-indigo-100 space-y-1">
                                                    <span className="text-[10px] font-black text-indigo-600 block">{entry.subject?.code || 'CS501'}</span>
                                                    <span className="font-bold text-slate-800 line-clamp-1">{entry.subject?.name || 'Algorithm Theory'}</span>
                                                    <span className="text-[10px] text-slate-500 block">{entry.room_number || 'Hall-301'}</span>
                                                </div>
                                            ) : (
                                                <div className="p-3 rounded-2xl bg-slate-50 border border-dashed border-slate-200 text-center text-[10px] text-slate-400 font-medium">
                                                    Self Study / Lab
                                                </div>
                                            )}
                                        </td>
                                    );
                                })}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default TimetableSchedulerPortal;
