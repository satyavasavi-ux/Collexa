import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import api from '../services/api';
import { Lock, Mail, Loader2, ShieldCheck, GraduationCap, BookOpen, UserCheck, DollarSign, Award, ArrowRight } from 'lucide-react';
import { jwtDecode } from 'jwt-decode';

const DEMO_ACCOUNTS = [
    { role: 'Admin', email: 'admin@collexa.edu', pass: 'admin123', color: 'from-purple-500 to-indigo-600', icon: ShieldCheck, desc: 'Super Admin Control Center' },
    { role: 'Teacher', email: 'teacher@collexa.edu', pass: 'teacher123', color: 'from-blue-500 to-cyan-600', icon: BookOpen, desc: 'Faculty & LMS Gradebook' },
    { role: 'Student', email: 'student@collexa.edu', pass: 'student123', color: 'from-emerald-500 to-teal-600', icon: GraduationCap, desc: 'Student Hub & Self-Service' },
    { role: 'Accounts', email: 'account@collexa.edu', pass: 'account123', color: 'from-amber-500 to-orange-600', icon: DollarSign, desc: 'Fee Invoicing & Finance' },
    { role: 'Exam Cell', email: 'exam@collexa.edu', pass: 'exam123', color: 'from-rose-500 to-pink-600', icon: Award, desc: 'Results & Hall Tickets' },
    { role: 'Admissions', email: 'admission@collexa.edu', pass: 'admission123', color: 'from-sky-500 to-blue-600', icon: UserCheck, desc: 'Applications & Enrollment' },
];

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const { user, login, loading: authLoading } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        if (!authLoading && user) {
            const role = user.role;
            if (role === 'ADMIN') navigate('/admin');
            else if (role === 'STUDENT') navigate('/student');
            else if (role === 'TEACHER') navigate('/teacher');
            else if (role === 'ADMISSION') navigate('/admission');
            else if (role === 'EXAM') navigate('/exam-cell');
            else if (role === 'ACCOUNT') navigate('/account-section');
        }
    }, [user, authLoading, navigate]);

    const handleLoginSubmit = async (loginEmail, loginPass) => {
        setLoading(true);
        setError('');
        try {
            const formData = new FormData();
            formData.append('username', loginEmail || email);
            formData.append('password', loginPass || password);

            const response = await api.post('/token', formData);
            login(response.data.access_token);

            const decoded = jwtDecode(response.data.access_token);
            const role = decoded.role;

            if (role === 'ADMIN') navigate('/admin');
            else if (role === 'STUDENT') navigate('/student');
            else if (role === 'TEACHER') navigate('/teacher');
            else if (role === 'ADMISSION') navigate('/admission');
            else if (role === 'EXAM') navigate('/exam-cell');
            else if (role === 'ACCOUNT') navigate('/account-section');
            else navigate('/');
        } catch (err) {
            const errorMsg = err.response?.data?.detail || 'Could not connect to server. Check backend connection.';
            setError(errorMsg === 'Incorrect email or password' ? 'Invalid email or password' : errorMsg);
        } finally {
            setLoading(false);
        }
    };

    const handleQuickLogin = (demo) => {
        setEmail(demo.email);
        setPassword(demo.pass);
        handleLoginSubmit(demo.email, demo.pass);
    };

    if (authLoading) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-slate-900 text-white">
                <Loader2 className="animate-spin h-10 w-10 text-indigo-500" />
            </div>
        );
    }

    return (
        <div className="min-h-screen flex flex-col justify-center py-12 px-4 sm:px-6 lg:px-8 bg-gradient-to-br from-slate-950 via-slate-900 to-indigo-950 text-slate-100">
            <div className="sm:mx-auto sm:w-full sm:max-w-md text-center">
                <div className="inline-flex p-3 rounded-2xl bg-indigo-600/20 border border-indigo-500/30 text-indigo-400 shadow-xl mb-4">
                    <ShieldCheck className="h-10 w-10" />
                </div>
                <h1 className="text-4xl font-black tracking-tight text-white">
                    COLLEXA<span className="text-indigo-400">.</span>
                </h1>
                <p className="mt-2 text-sm font-semibold uppercase tracking-widest text-indigo-300/70">
                    Enterprise Campus ERP & Academic Ecosystem
                </p>
            </div>

            <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-xl">
                <div className="bg-slate-900/80 backdrop-blur-xl py-8 px-6 shadow-2xl rounded-3xl sm:px-10 border border-slate-800">
                    {error && (
                        <div className="mb-6 p-4 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-300 text-sm font-medium">
                            {error}
                        </div>
                    )}

                    <form className="space-y-5" onSubmit={(e) => { e.preventDefault(); handleLoginSubmit(); }}>
                        <div>
                            <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">
                                Institutional Email
                            </label>
                            <div className="relative">
                                <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-500">
                                    <Mail className="h-4 w-4" />
                                </div>
                                <input
                                    type="email"
                                    required
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    placeholder="your.email@collexa.edu"
                                    className="w-full pl-10 pr-4 py-3 bg-slate-800/80 border border-slate-700 rounded-xl text-white placeholder-slate-500 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
                                />
                            </div>
                        </div>

                        <div>
                            <label className="block text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">
                                Secure Password
                            </label>
                            <div className="relative">
                                <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-500">
                                    <Lock className="h-4 w-4" />
                                </div>
                                <input
                                    type="password"
                                    required
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    placeholder="••••••••••••"
                                    className="w-full pl-10 pr-4 py-3 bg-slate-800/80 border border-slate-700 rounded-xl text-white placeholder-slate-500 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition-all"
                                />
                            </div>
                        </div>

                        <button
                            type="submit"
                            disabled={loading}
                            className="w-full flex items-center justify-center py-3.5 px-4 rounded-xl text-sm font-bold text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 shadow-lg shadow-indigo-600/30 transition-all disabled:opacity-50"
                        >
                            {loading ? (
                                <Loader2 className="animate-spin h-5 w-5" />
                            ) : (
                                <>
                                    <span>Access Dashboard</span>
                                    <ArrowRight className="ml-2 h-4 w-4" />
                                </>
                            )}
                        </button>
                    </form>

                    {/* Quick Demo Switcher */}
                    <div className="mt-8 pt-6 border-t border-slate-800">
                        <p className="text-xs font-black uppercase tracking-widest text-slate-400 text-center mb-4">
                            ⚡ Quick 1-Click Role Logins (Demo Data Ready)
                        </p>
                        <div className="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                            {DEMO_ACCOUNTS.map((demo) => {
                                const Icon = demo.icon;
                                return (
                                    <button
                                        key={demo.role}
                                        type="button"
                                        onClick={() => handleQuickLogin(demo)}
                                        className="p-3 rounded-xl bg-slate-800/50 hover:bg-slate-800 border border-slate-700/60 hover:border-indigo-500/50 text-left transition-all group"
                                    >
                                        <div className="flex items-center space-x-2 mb-1">
                                            <div className={`p-1.5 rounded-lg bg-gradient-to-br ${demo.color} text-white shadow-sm`}>
                                                <Icon className="h-3.5 w-3.5" />
                                            </div>
                                            <span className="text-xs font-bold text-white group-hover:text-indigo-400 transition-colors">
                                                {demo.role}
                                            </span>
                                        </div>
                                        <p className="text-[10px] text-slate-400 truncate">{demo.desc}</p>
                                    </button>
                                );
                            })}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Login;
