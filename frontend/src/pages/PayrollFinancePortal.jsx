import React, { useState, useEffect } from 'react';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { DollarSign, FileText, Download, User, Calendar, ShieldCheck, CheckCircle2 } from 'lucide-react';

const PayrollFinancePortal = () => {
    const { user } = useAuth();
    const [slip, setSlip] = useState(null);

    useEffect(() => {
        fetchSlip();
    }, []);

    const fetchSlip = async () => {
        try {
            const res = await api.get(`/api/payroll/slip/${user?.id || 'EMP-1001'}`);
            setSlip(res.data);
        } catch (err) {
            console.error('Failed to load salary slip', err);
        }
    };

    return (
        <div className="space-y-8 animate-fade-in">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-emerald-950 via-teal-950 to-slate-950 p-8 rounded-3xl text-white shadow-xl">
                <div>
                    <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-bold uppercase tracking-wider mb-3">
                        <DollarSign className="h-3.5 w-3.5" />
                        <span>Finance & Compensation Management</span>
                    </div>
                    <h1 className="text-3xl font-black tracking-tight">Faculty & Staff Payroll Terminal</h1>
                    <p className="text-slate-300 text-sm mt-1">Access monthly tax itemized compensation slips, allowance breakdowns, and PF statements.</p>
                </div>
            </div>

            {slip && (
                <div className="bg-white rounded-3xl p-8 border border-slate-200 shadow-sm space-y-6 max-w-4xl mx-auto">
                    <div className="flex justify-between items-center pb-6 border-b border-slate-100">
                        <div>
                            <span className="text-xs font-bold text-emerald-600 uppercase tracking-widest">Collexa Autonomous University</span>
                            <h2 className="text-2xl font-black text-slate-800 mt-1">Monthly Salary Slip</h2>
                            <p className="text-xs text-slate-500">Period: August 2026 • Days Worked: {slip.days_worked}</p>
                        </div>
                        <div className="text-right">
                            <span className="text-xs font-bold text-slate-400 uppercase">Net Disbursed</span>
                            <h3 className="text-3xl font-black text-emerald-600">₹{slip.net_salary_payable.toLocaleString()}</h3>
                        </div>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                        {/* Earnings */}
                        <div className="space-y-4">
                            <h3 className="text-xs font-black uppercase tracking-wider text-slate-400">Earnings & Allowances</h3>
                            <div className="space-y-2 text-xs">
                                <div className="flex justify-between p-3 rounded-xl bg-slate-50"><span>Basic Pay</span><span className="font-bold">₹{slip.earnings.basic_pay.toLocaleString()}</span></div>
                                <div className="flex justify-between p-3 rounded-xl bg-slate-50"><span>House Rent Allowance (HRA)</span><span className="font-bold">₹{slip.earnings.house_rent_allowance.toLocaleString()}</span></div>
                                <div className="flex justify-between p-3 rounded-xl bg-slate-50"><span>Dearness Allowance (DA)</span><span className="font-bold">₹{slip.earnings.dearness_allowance.toLocaleString()}</span></div>
                                <div className="flex justify-between p-3 rounded-xl bg-slate-50"><span>Travel Allowance</span><span className="font-bold">₹{slip.earnings.travel_allowance.toLocaleString()}</span></div>
                                <div className="flex justify-between p-3 rounded-xl bg-emerald-50 text-emerald-800 font-bold"><span>Gross Salary</span><span>₹{slip.earnings.gross_salary.toLocaleString()}</span></div>
                            </div>
                        </div>

                        {/* Deductions */}
                        <div className="space-y-4">
                            <h3 className="text-xs font-black uppercase tracking-wider text-slate-400">Deductions & Taxes</h3>
                            <div className="space-y-2 text-xs">
                                <div className="flex justify-between p-3 rounded-xl bg-slate-50"><span>Provident Fund (PF)</span><span className="font-bold">₹{slip.deductions.provident_fund.toLocaleString()}</span></div>
                                <div className="flex justify-between p-3 rounded-xl bg-slate-50"><span>Professional Tax</span><span className="font-bold">₹{slip.deductions.professional_tax.toLocaleString()}</span></div>
                                <div className="flex justify-between p-3 rounded-xl bg-slate-50"><span>Tax Deducted at Source (TDS)</span><span className="font-bold">₹{slip.deductions.tax_deducted_at_source.toLocaleString()}</span></div>
                                <div className="flex justify-between p-3 rounded-xl bg-rose-50 text-rose-800 font-bold"><span>Total Deductions</span><span>₹{slip.deductions.total_deductions.toLocaleString()}</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default PayrollFinancePortal;
