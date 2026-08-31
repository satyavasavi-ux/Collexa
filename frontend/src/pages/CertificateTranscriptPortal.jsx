import React, { useState } from 'react';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { Award, Download, ShieldCheck, CheckCircle2 } from 'lucide-react';

const CertificateTranscriptPortal = () => {
    const { user } = useAuth();
    const [certificate, setCertificate] = useState(null);

    const handleGenerateCertificate = async () => {
        try {
            const res = await api.get(`/api/certificates/bonafide/${user?.id || 1}`);
            setCertificate(res.data);
        } catch (err) {
            alert('Failed to generate bonafide certificate');
        }
    };

    return (
        <div className="space-y-8 animate-fade-in max-w-3xl mx-auto">
            <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 p-8 rounded-3xl text-white shadow-xl flex justify-between items-center">
                <div>
                    <h1 className="text-2xl font-black">Official Academic Certificates</h1>
                    <p className="text-xs text-slate-300 mt-1">Generate digitally signed bonafide and transcript certificates.</p>
                </div>
                <button
                    onClick={handleGenerateCertificate}
                    className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-md"
                >
                    Issue Bonafide Certificate
                </button>
            </div>

            {certificate && (
                <div className="bg-white p-10 rounded-3xl border border-slate-300 shadow-xl space-y-6 text-center border-t-8 border-t-indigo-600">
                    <div className="space-y-1">
                        <span className="text-[10px] font-black uppercase tracking-widest text-indigo-600">Collexa Autonomous University</span>
                        <h2 className="text-xl font-black text-slate-900">{certificate.title}</h2>
                        <p className="text-[10px] font-mono text-slate-400">ID: {certificate.certificate_id}</p>
                    </div>

                    <p className="text-sm text-slate-700 leading-loose py-4 max-w-xl mx-auto italic font-serif">
                        "{certificate.body_text}"
                    </p>

                    <div className="pt-6 border-t border-slate-100 flex justify-between items-end text-left text-xs">
                        <div>
                            <span className="text-[10px] text-slate-400 block font-bold">Issue Date</span>
                            <span className="font-bold text-slate-700">{certificate.issue_date}</span>
                        </div>
                        <div className="text-right">
                            <span className="text-[10px] text-slate-400 block font-bold">Digital Signature Seal</span>
                            <span className="text-[9px] font-mono text-indigo-600 truncate max-w-xs block">{certificate.digital_signature_hash}</span>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default CertificateTranscriptPortal;
