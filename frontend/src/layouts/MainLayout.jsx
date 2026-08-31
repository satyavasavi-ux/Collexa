import React from 'react';
import { Link, useNavigate, useLocation, Outlet } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import {
    LayoutDashboard,
    User,
    Calendar,
    FileText,
    LogOut,
    QrCode,
    CreditCard,
    Settings,
    ClipboardList,
    MessageSquare,
    GraduationCap,
    ShieldCheck,
    Wallet,
    BookOpen,
    Briefcase,
    Home,
    Sparkles,
    BarChart3,
    Compass,
    Video,
    Award,
    DollarSign,
    Package,
    Users,
    Star,
    AlertCircle
} from 'lucide-react';

const MainLayout = () => {
    const { user, logout } = useAuth();
    const navigate = useNavigate();
    const location = useLocation();

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    const menuItems = {
        STUDENT: [
            { name: 'Student Hub', path: '/student', icon: LayoutDashboard },
            { name: 'Course LMS & Notes', path: '/student/lms', icon: BookOpen },
            { name: 'Scan Attendance', path: '/student/scan', icon: QrCode },
            { name: 'Digital ID Pass', path: '/student/id-card', icon: ShieldCheck },
            { name: 'Online Exam & Proctor', path: '/student/exam-proctor', icon: Video },
            { name: 'Digital Library', path: '/student/library', icon: BookOpen },
            { name: 'Placement & Careers', path: '/student/placements', icon: Briefcase },
            { name: 'Hostel & Transport', path: '/student/hostel-transport', icon: Home },
            { name: 'Scholarships & Grants', path: '/student/scholarships', icon: Award },
            { name: 'Bonafide Certificates', path: '/student/certificates', icon: FileText },
            { name: 'Faculty Appraisal', path: '/student/feedback', icon: Star },
            { name: 'Grievance Desk', path: '/student/grievances', icon: AlertCircle },
            { name: 'Events & Hackathons', path: '/student/events', icon: Compass },
            { name: 'Campus Chat', path: '/student/chat', icon: MessageSquare },
            { name: 'AI Academic Tutor', path: '/student/ai-tutor', icon: Sparkles },
        ],
        TEACHER: [
            { name: 'Faculty Dashboard', path: '/teacher', icon: LayoutDashboard },
            { name: 'Course LMS & Gradebook', path: '/teacher/lms', icon: BookOpen },
            { name: 'Timetable Matrix', path: '/timetable-scheduler', icon: Calendar },
            { name: 'Salary Slips & Payroll', path: '/payroll', icon: DollarSign },
            { name: 'Library Catalog', path: '/library', icon: BookOpen },
            { name: 'Campus Chat', path: '/chat', icon: MessageSquare },
            { name: 'AI Assistant', path: '/ai-assistant', icon: Sparkles },
        ],
        ADMIN: [
            { name: 'Super Admin Hub', path: '/admin', icon: ShieldCheck },
            { name: 'Executive BI Analytics', path: '/admin/analytics', icon: BarChart3 },
            { name: 'Timetable Scheduler', path: '/timetable-scheduler', icon: Calendar },
            { name: 'Course LMS & Syllabus', path: '/admin/lms', icon: BookOpen },
            { name: 'Staff & Faculty Payroll', path: '/payroll', icon: DollarSign },
            { name: 'Asset Inventory & Labs', path: '/inventory', icon: Package },
            { name: 'Alumni Network', path: '/alumni', icon: Users },
            { name: 'Scholarships Portal', path: '/scholarships', icon: Award },
            { name: 'Library Management', path: '/library', icon: BookOpen },
            { name: 'Placement Cell', path: '/placements', icon: Briefcase },
            { name: 'Hostel & Fleet', path: '/hostel-transport', icon: Home },
            { name: 'Events & Hackathons', path: '/events', icon: Compass },
            { name: 'Campus Chat', path: '/chat', icon: MessageSquare },
            { name: 'AI Intelligence', path: '/ai-assistant', icon: Sparkles },
        ],
        ADMISSION: [
            { name: 'Admission Portal', path: '/admission', icon: GraduationCap },
            { name: 'Campus Chat', path: '/chat', icon: MessageSquare },
        ],
        EXAM: [
            { name: 'Exam Cell Operations', path: '/exam-cell', icon: ClipboardList },
            { name: 'Analytics & Trends', path: '/admin/analytics', icon: BarChart3 },
            { name: 'Campus Chat', path: '/chat', icon: MessageSquare },
        ],
        ACCOUNT: [
            { name: 'Account Section', path: '/account-section', icon: Wallet },
            { name: 'Payroll & Invoicing', path: '/payroll', icon: DollarSign },
            { name: 'Asset Inventory', path: '/inventory', icon: Package },
            { name: 'Financial Analytics', path: '/admin/analytics', icon: BarChart3 },
            { name: 'Campus Chat', path: '/chat', icon: MessageSquare },
        ],
    };

    const currentMenu = menuItems[user?.role] || [];

    return (
        <div className="flex h-screen bg-brand-bg text-brand-text overflow-hidden">
            {/* Sidebar */}
            <aside className="w-72 bg-[#0b1329] border-r border-slate-800/80 flex flex-col shadow-2xl z-20">
                <div className="p-6 pb-4">
                    <div className="flex items-center space-x-3 mb-1">
                        <div className="h-10 w-10 bg-indigo-600 rounded-2xl flex items-center justify-center shadow-lg shadow-indigo-600/30">
                            <ShieldCheck className="text-white h-6 w-6" />
                        </div>
                        <div>
                            <h1 className="text-xl font-black text-white tracking-tighter italic">
                                COLLEXA<span className="text-indigo-500">.</span>
                            </h1>
                            <p className="text-[9px] text-indigo-400/80 font-black uppercase tracking-[0.25em]">Enterprise ERP</p>
                        </div>
                    </div>
                </div>

                <nav className="flex-1 px-4 space-y-1 overflow-y-auto custom-scrollbar pt-2">
                    <div className="px-3 py-1.5 text-[10px] font-black uppercase tracking-widest text-slate-500">
                        {user?.role} Workspace
                    </div>
                    {currentMenu.map((item) => {
                        const isActive = location.pathname === item.path;
                        const Icon = item.icon;
                        return (
                            <Link
                                key={item.name}
                                to={item.path}
                                className={`flex items-center px-4 py-2.5 text-xs font-bold rounded-2xl transition-all duration-200 group ${
                                    isActive
                                        ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/25 scale-[1.01]'
                                        : 'text-slate-400 hover:bg-slate-800/60 hover:text-white'
                                }`}
                            >
                                <Icon className={`mr-3 h-4 w-4 transition-transform group-hover:scale-110 ${isActive ? 'text-white' : 'text-slate-500 group-hover:text-indigo-400'}`} />
                                <span className="truncate">{item.name}</span>
                            </Link>
                        );
                    })}
                </nav>

                <div className="p-4 mt-auto">
                    <div className="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 shadow-inner">
                        <div className="flex items-center mb-3">
                            <div className="h-10 w-10 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-xs font-black text-white shadow-md">
                                {user?.name?.[0]?.toUpperCase() || 'U'}
                            </div>
                            <div className="ml-3 overflow-hidden">
                                <p className="text-xs font-black text-white truncate leading-none mb-1">{user?.name}</p>
                                <span className="inline-block text-[9px] font-black text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded-md uppercase tracking-wider border border-indigo-500/20">
                                    {user?.role}
                                </span>
                            </div>
                        </div>
                        <button
                            onClick={handleLogout}
                            className="flex items-center justify-center w-full py-2 bg-rose-500/10 text-rose-400 text-[10px] font-black uppercase tracking-wider rounded-xl hover:bg-rose-600 hover:text-white transition-all border border-rose-500/20"
                        >
                            <LogOut className="mr-2 h-3.5 w-3.5" />
                            Sign Out
                        </button>
                    </div>
                </div>
            </aside>

            {/* Main Content Area */}
            <main className="flex-1 overflow-y-auto bg-slate-50 p-6 md:p-10">
                <div className="max-w-7xl mx-auto">
                    <Outlet />
                </div>
            </main>
        </div>
    );
};

export default MainLayout;
