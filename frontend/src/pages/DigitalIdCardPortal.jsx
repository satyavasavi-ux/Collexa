import React from 'react';
import { useAuth } from '../context/AuthContext';
import { ShieldCheck, QrCode, CreditCard, Sparkles } from 'lucide-react';

const DigitalIdCardPortal = () => {
    const { user } = useAuth();

    return (
        <div className="space-y-8 animate-fade-in max-w-xl mx-auto">
            <div className="text-center space-y-2">
                <h1 className="text-3xl font-black text-slate-800">Digital Identity Credential</h1>
                <p className="text-xs text-slate-500">Official student NFC/QR smart identity pass.</p>
            </div>

            {/* Smart Card */}
            <div className="bg-gradient-to-br from-[#0f172a] via-[#1e1b4b] to-[#31104b] p-8 rounded-3xl text-white shadow-2xl border border-purple-500/30 space-y-6 relative overflow-hidden">
                <div className="flex justify-between items-start">
                    <div className="flex items-center space-x-3">
                        <div className="p-2.5 rounded-2xl bg-indigo-600/30 border border-indigo-500/40 text-indigo-400">
                            <ShieldCheck className="h-6 w-6" />
                        </div>
                        <div>
                            <h2 className="text-lg font-black tracking-wider italic">COLLEXA.</h2>
                            <p className="text-[9px] uppercase tracking-widest text-indigo-300 font-bold">Autonomous University</p>
                        </div>
                    </div>
                    <span className="px-3 py-1 rounded-full bg-white/10 text-[10px] font-black uppercase tracking-wider">{user?.role}</span>
                </div>

                <div className="flex items-center space-x-5 py-4">
                    <div className="h-20 w-20 rounded-2xl bg-gradient-to-br from-indigo-500 to-pink-500 flex items-center justify-center text-3xl font-black text-white shadow-lg">
                        {user?.name?.[0]}
                    </div>
                    <div className="space-y-1">
                        <h3 className="text-xl font-black">{user?.name}</h3>
                        <p className="text-xs font-mono text-indigo-300">{user?.student_profile?.roll_number || 'COL24CS001'}</p>
                        <p className="text-xs text-slate-300">{user?.student_profile?.department || 'Computer Science'}</p>
                    </div>
                </div>

                <div className="pt-4 border-t border-white/10 flex justify-between items-center">
                    <div className="text-[10px] text-slate-400">
                        <p>Valid Until: June 2027</p>
                        <p>Blood Group: O+ • Batch: 2023-27</p>
                    </div>
                    <div className="p-2 bg-white rounded-xl">
                        <QrCode className="h-8 w-8 text-slate-900" />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default DigitalIdCardPortal;
