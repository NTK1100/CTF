package androidx.startup;

import android.util.Log;

/* loaded from: classes.dex */
public final class StartupLogger {
    static final boolean DEBUG = false;
    private static final String TAG = "StartupLogger";

    private StartupLogger() {
    }

    /* renamed from: i */
    public static void m44i(String str) {
        Log.i(TAG, str);
    }

    /* renamed from: w */
    public static void m43w(String str) {
        Log.w(TAG, str);
    }

    /* renamed from: e */
    public static void m45e(String str, Throwable th) {
        Log.e(TAG, str, th);
    }
}