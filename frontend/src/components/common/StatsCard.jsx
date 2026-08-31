import React from 'react';
import { TrendingUp, TrendingDown } from 'lucide-react';

const StatsCard = ({ title, value, subtitle, icon: Icon, trend, trendValue, color = "indigo" }) => {
    const colorClasses = {
        indigo: "bg-indigo-50 text-indigo-600 border-indigo-200",
        emerald: "bg-emerald-50 text-emerald-600 border-emerald-200",
        purple: "bg-purple-50 text-purple-600 border-purple-200",
        amber: "bg-amber-50 text-amber-600 border-amber-200",
        rose: "bg-rose-50 text-rose-600 border-rose-200",
        blue: "bg-blue-50 text-blue-600 border-blue-200"
    };

    return (
        <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-3 hover:shadow-md transition-all">
            <div className="flex justify-between items-start">
                <div className={`p-3 rounded-2xl border ${colorClasses[color] || colorClasses.indigo}`}>
                    {Icon && <Icon className="h-5 w-5" />}
                </div>
                {trend && (
                    <span className={`inline-flex items-center text-[10px] font-black px-2 py-0.5 rounded-full ${
                        trend === 'up' ? 'bg-emerald-100 text-emerald-700' : 'bg-rose-100 text-rose-700'
                    }`}>
                        {trend === 'up' ? <TrendingUp className="h-3 w-3 mr-1" /> : <TrendingDown className="h-3 w-3 mr-1" />}
                        {trendValue}
                    </span>
                )}
            </div>
            <div>
                <span className="text-[10px] font-black uppercase tracking-wider text-slate-400">{title}</span>
                <h3 className="text-2xl font-black text-slate-800 mt-0.5">{value}</h3>
                {subtitle && <p className="text-xs text-slate-500 mt-1">{subtitle}</p>}
            </div>
        </div>
    );
};

export default StatsCard;
