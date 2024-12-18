use App\Http\Controllers\EmailController;

Route::get('/email/form', [EmailController::class, 'showForm'])->name('email.form');
Route::post('/email/send', [EmailController::class, 'sendEmail'])->name('send.email');
