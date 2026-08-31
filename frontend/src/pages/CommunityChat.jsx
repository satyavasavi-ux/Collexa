import React, { useState, useEffect, useRef } from 'react';
import api from '../services/api';
import { useAuth } from '../context/AuthContext';
import { MessageSquare, Send, Users, Hash, Shield, Sparkles } from 'lucide-react';

const CommunityChat = () => {
    const { user } = useAuth();
    const [channels, setChannels] = useState([]);
    const [selectedChannel, setSelectedChannel] = useState(null);
    const [messages, setMessages] = useState([]);
    const [inputMsg, setInputMsg] = useState('');
    const messagesEndRef = useRef(null);

    useEffect(() => {
        fetchChannels();
    }, []);

    useEffect(() => {
        if (selectedChannel) {
            fetchMessages(selectedChannel.id);
            const interval = setInterval(() => fetchMessages(selectedChannel.id), 3000);
            return () => clearInterval(interval);
        }
    }, [selectedChannel]);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    const fetchChannels = async () => {
        try {
            const res = await api.get('/api/chat/channels');
            setChannels(res.data);
            if (res.data.length > 0) {
                setSelectedChannel(res.data[0]);
            }
        } catch (err) {
            console.error('Failed to load chat channels', err);
        }
    };

    const fetchMessages = async (channelId) => {
        try {
            const res = await api.get(`/api/chat/channels/${channelId}/messages`);
            setMessages(res.data);
        } catch (err) {
            console.error('Failed to fetch messages', err);
        }
    };

    const handleSendMessage = async (e) => {
        e.preventDefault();
        if (!inputMsg.trim() || !selectedChannel) return;
        try {
            await api.post(`/api/chat/channels/${selectedChannel.id}/messages`, {
                channel_id: selectedChannel.id,
                content: inputMsg
            });
            setInputMsg('');
            fetchMessages(selectedChannel.id);
        } catch (err) {
            console.error('Failed to send message', err);
        }
    };

    return (
        <div className="space-y-6 animate-fade-in">
            {/* Header */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 p-6 rounded-3xl text-white shadow-xl">
                <div>
                    <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-indigo-500/20 text-indigo-300 text-xs font-bold uppercase tracking-wider mb-2">
                        <MessageSquare className="h-3.5 w-3.5" />
                        <span>Campus Real-Time Collaboration</span>
                    </div>
                    <h1 className="text-2xl font-black tracking-tight">Community Channels & Study Groups</h1>
                </div>
            </div>

            {/* Chat App Card */}
            <div className="bg-white rounded-3xl border border-slate-200 shadow-sm overflow-hidden grid grid-cols-1 md:grid-cols-4 h-[600px]">
                {/* Channels Sidebar */}
                <div className="md:col-span-1 border-r border-slate-200 bg-slate-50/50 p-4 space-y-3 overflow-y-auto">
                    <h3 className="text-xs font-black uppercase tracking-widest text-slate-400 px-2">Channels</h3>
                    <div className="space-y-1">
                        {channels.map((ch) => (
                            <button
                                key={ch.id}
                                onClick={() => setSelectedChannel(ch)}
                                className={`w-full text-left p-3 rounded-2xl flex items-center space-x-2.5 transition-all ${
                                    selectedChannel?.id === ch.id
                                        ? 'bg-indigo-600 text-white shadow-md font-bold'
                                        : 'text-slate-600 hover:bg-slate-200/60'
                                }`}
                            >
                                <Hash className="h-4 w-4 opacity-70" />
                                <span className="text-xs truncate">{ch.name}</span>
                            </button>
                        ))}
                    </div>
                </div>

                {/* Chat Messages Panel */}
                <div className="md:col-span-3 flex flex-col h-full bg-white">
                    {selectedChannel && (
                        <>
                            {/* Channel Header */}
                            <div className="p-4 border-b border-slate-100 flex items-center justify-between bg-slate-50/30">
                                <div>
                                    <h4 className="text-sm font-black text-slate-800 flex items-center">
                                        <Hash className="h-4 w-4 mr-1 text-indigo-600" />
                                        {selectedChannel.name}
                                    </h4>
                                    <p className="text-[10px] text-slate-500">{selectedChannel.description}</p>
                                </div>
                            </div>

                            {/* Message Log */}
                            <div className="flex-1 p-6 overflow-y-auto space-y-4 bg-slate-50/20">
                                {messages.map((m) => {
                                    const isMe = m.sender_id === user?.id;
                                    return (
                                        <div key={m.id} className={`flex flex-col ${isMe ? 'items-end' : 'items-start'}`}>
                                            <div className="flex items-center space-x-2 mb-1">
                                                <span className="text-[10px] font-bold text-slate-500">{m.sender?.name || (isMe ? 'You' : `User #${m.sender_id}`)}</span>
                                                <span className="text-[9px] text-slate-400">{new Date(m.sent_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                                            </div>
                                            <div className={`p-3.5 rounded-2xl text-xs max-w-md ${
                                                isMe ? 'bg-indigo-600 text-white rounded-br-none shadow-sm' : 'bg-white text-slate-800 border border-slate-200 rounded-bl-none shadow-sm'
                                            }`}>
                                                {m.content}
                                            </div>
                                        </div>
                                    );
                                })}
                                <div ref={messagesEndRef} />
                            </div>

                            {/* Input Form */}
                            <form onSubmit={handleSendMessage} className="p-4 border-t border-slate-100 bg-white flex space-x-3">
                                <input
                                    type="text"
                                    value={inputMsg}
                                    onChange={(e) => setInputMsg(e.target.value)}
                                    placeholder={`Message #${selectedChannel.name}...`}
                                    className="flex-1 px-4 py-3 bg-slate-50 border border-slate-200 rounded-2xl text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                                />
                                <button
                                    type="submit"
                                    className="px-5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-2xl shadow-md flex items-center justify-center transition-all"
                                >
                                    <Send className="h-4 w-4" />
                                </button>
                            </form>
                        </>
                    )}
                </div>
            </div>
        </div>
    );
};

export default CommunityChat;
