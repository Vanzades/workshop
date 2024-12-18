<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;

class EmailController extends Controller
{
    public function sendEmail(Request $request)
    {
        $request->validate([
            'email' => 'required|email',
            'subject' => 'required|string|max:255',
            'message' => 'required|string',
        ]);

        $emailData = [
            'recipient' => $request->email,
            'subject' => $request->subject,
            'body' => $request->message,
        ];

        Mail::send('emails.template', ['body' => $emailData['body']], function ($message) use ($emailData) {
            $message->to($emailData['recipient'])
                    ->subject($emailData['subject']);
        });

        return back()->with('success', 'Email sent successfully!');
    }

    public function showForm()
    {
        return view('emails.form');
    }
}
