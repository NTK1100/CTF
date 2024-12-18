package androidx.constraintlayout.core.motion.utils;

/* loaded from: classes.dex */
public class LinearCurveFit extends CurveFit {
    private static final String TAG = "LinearCurveFit";
    private boolean mExtrapolate = true;
    double[] mSlopeTemp;

    /* renamed from: mT */
    private double[] f28mT;
    private double mTotalLength;

    /* renamed from: mY */
    private double[][] f29mY;

    public LinearCurveFit(double[] time, double[][] y) {
        int dim;
        double px;
        this.mTotalLength = Double.NaN;
        int length = time.length;
        char c = 0;
        int dim2 = y[0].length;
        this.mSlopeTemp = new double[dim2];
        this.f28mT = time;
        this.f29mY = y;
        if (dim2 > 2) {
            double sum = 0.0d;
            double lastx = 0.0d;
            double lasty = 0.0d;
            int i = 0;
            while (i < time.length) {
                double px2 = y[i][c];
                double py = y[i][c];
                if (i <= 0) {
                    dim = dim2;
                    px = px2;
                } else {
                    dim = dim2;
                    px = px2;
                    sum += Math.hypot(px2 - lastx, py - lasty);
                }
                lastx = px;
                lasty = py;
                i++;
                dim2 = dim;
                c = 0;
            }
            this.mTotalLength = 0.0d;
        }
    }

    private double getLength2D(double t) {
        double px;
        if (Double.isNaN(this.mTotalLength)) {
            return 0.0d;
        }
        double[] dArr = this.f28mT;
        int n = dArr.length;
        if (t <= dArr[0]) {
            return 0.0d;
        }
        if (t >= dArr[n - 1]) {
            return this.mTotalLength;
        }
        double sum = 0.0d;
        double last_x = 0.0d;
        double last_y = 0.0d;
        for (int i = 0; i < n - 1; i++) {
            double[][] dArr2 = this.f29mY;
            double px2 = dArr2[i][0];
            double py = dArr2[i][1];
            if (i <= 0) {
                px = px2;
            } else {
                px = px2;
                sum += Math.hypot(px2 - last_x, py - last_y);
            }
            last_x = px;
            last_y = py;
            double[] dArr3 = this.f28mT;
            if (t == dArr3[i]) {
                return sum;
            }
            if (t < dArr3[i + 1]) {
                double h = dArr3[i + 1] - dArr3[i];
                double x = (t - dArr3[i]) / h;
                double[][] dArr4 = this.f29mY;
                double x1 = dArr4[i][0];
                double x2 = dArr4[i + 1][0];
                double y1 = dArr4[i][1];
                double y2 = dArr4[i + 1][1];
                return sum + Math.hypot(py - (((1.0d - x) * y1) + (y2 * x)), px - (((1.0d - x) * x1) + (x2 * x)));
            }
        }
        return 0.0d;
    }

    @Override // androidx.constraintlayout.core.motion.utils.CurveFit
    public void getPos(double t, double[] v) {
        double[] dArr = this.f28mT;
        int n = dArr.length;
        int dim = this.f29mY[0].length;
        if (this.mExtrapolate) {
            if (t <= dArr[0]) {
                getSlope(dArr[0], this.mSlopeTemp);
                for (int j = 0; j < dim; j++) {
                    v[j] = this.f29mY[0][j] + ((t - this.f28mT[0]) * this.mSlopeTemp[j]);
                }
                return;
            } else if (t >= dArr[n - 1]) {
                getSlope(dArr[n - 1], this.mSlopeTemp);
                for (int j2 = 0; j2 < dim; j2++) {
                    v[j2] = this.f29mY[n - 1][j2] + ((t - this.f28mT[n - 1]) * this.mSlopeTemp[j2]);
                }
                return;
            }
        } else if (t <= dArr[0]) {
            for (int j3 = 0; j3 < dim; j3++) {
                v[j3] = this.f29mY[0][j3];
            }
            return;
        } else if (t >= dArr[n - 1]) {
            for (int j4 = 0; j4 < dim; j4++) {
                v[j4] = this.f29mY[n - 1][j4];
            }
            return;
        }
        for (int i = 0; i < n - 1; i++) {
            if (t == this.f28mT[i]) {
                for (int j5 = 0; j5 < dim; j5++) {
                    v[j5] = this.f29mY[i][j5];
                }
            }
            double[] dArr2 = this.f28mT;
            if (t < dArr2[i + 1]) {
                double h = dArr2[i + 1] - dArr2[i];
                double x = (t - dArr2[i]) / h;
                for (int j6 = 0; j6 < dim; j6++) {
                    double[][] dArr3 = this.f29mY;
                    double y1 = dArr3[i][j6];
                    double y2 = dArr3[i + 1][j6];
                    v[j6] = ((1.0d - x) * y1) + (y2 * x);
                }
                return;
            }
        }
    }

    @Override // androidx.constraintlayout.core.motion.utils.CurveFit
    public void getPos(double t, float[] v) {
        double[] dArr = this.f28mT;
        int n = dArr.length;
        int dim = this.f29mY[0].length;
        if (this.mExtrapolate) {
            if (t <= dArr[0]) {
                getSlope(dArr[0], this.mSlopeTemp);
                for (int j = 0; j < dim; j++) {
                    v[j] = (float) (this.f29mY[0][j] + ((t - this.f28mT[0]) * this.mSlopeTemp[j]));
                }
                return;
            } else if (t >= dArr[n - 1]) {
                getSlope(dArr[n - 1], this.mSlopeTemp);
                for (int j2 = 0; j2 < dim; j2++) {
                    v[j2] = (float) (this.f29mY[n - 1][j2] + ((t - this.f28mT[n - 1]) * this.mSlopeTemp[j2]));
                }
                return;
            }
        } else if (t <= dArr[0]) {
            for (int j3 = 0; j3 < dim; j3++) {
                v[j3] = (float) this.f29mY[0][j3];
            }
            return;
        } else if (t >= dArr[n - 1]) {
            for (int j4 = 0; j4 < dim; j4++) {
                v[j4] = (float) this.f29mY[n - 1][j4];
            }
            return;
        }
        for (int i = 0; i < n - 1; i++) {
            if (t == this.f28mT[i]) {
                for (int j5 = 0; j5 < dim; j5++) {
                    v[j5] = (float) this.f29mY[i][j5];
                }
            }
            double[] dArr2 = this.f28mT;
            if (t < dArr2[i + 1]) {
                double h = dArr2[i + 1] - dArr2[i];
                double x = (t - dArr2[i]) / h;
                for (int j6 = 0; j6 < dim; j6++) {
                    double[][] dArr3 = this.f29mY;
                    double y1 = dArr3[i][j6];
                    double y2 = dArr3[i + 1][j6];
                    v[j6] = (float) (((1.0d - x) * y1) + (y2 * x));
                }
                return;
            }
        }
    }

    @Override // androidx.constraintlayout.core.motion.utils.CurveFit
    public double getPos(double t, int j) {
        double[] dArr = this.f28mT;
        int n = dArr.length;
        if (this.mExtrapolate) {
            if (t <= dArr[0]) {
                return this.f29mY[0][j] + ((t - dArr[0]) * getSlope(dArr[0], j));
            }
            if (t >= dArr[n - 1]) {
                return this.f29mY[n - 1][j] + ((t - dArr[n - 1]) * getSlope(dArr[n - 1], j));
            }
        } else if (t <= dArr[0]) {
            return this.f29mY[0][j];
        } else {
            if (t >= dArr[n - 1]) {
                return this.f29mY[n - 1][j];
            }
        }
        for (int i = 0; i < n - 1; i++) {
            double[] dArr2 = this.f28mT;
            if (t == dArr2[i]) {
                return this.f29mY[i][j];
            }
            if (t < dArr2[i + 1]) {
                double h = dArr2[i + 1] - dArr2[i];
                double x = (t - dArr2[i]) / h;
                double[][] dArr3 = this.f29mY;
                double y1 = dArr3[i][j];
                double y2 = dArr3[i + 1][j];
                return ((1.0d - x) * y1) + (y2 * x);
            }
        }
        return 0.0d;
    }

    @Override // androidx.constraintlayout.core.motion.utils.CurveFit
    public void getSlope(double t, double[] v) {
        double t2;
        double[] dArr = this.f28mT;
        int n = dArr.length;
        int dim = this.f29mY[0].length;
        if (t <= dArr[0]) {
            t2 = dArr[0];
        } else if (t < dArr[n - 1]) {
            t2 = t;
        } else {
            t2 = dArr[n - 1];
        }
        for (int i = 0; i < n - 1; i++) {
            double[] dArr2 = this.f28mT;
            if (t2 <= dArr2[i + 1]) {
                double h = dArr2[i + 1] - dArr2[i];
                double d = (t2 - dArr2[i]) / h;
                for (int j = 0; j < dim; j++) {
                    double[][] dArr3 = this.f29mY;
                    double y1 = dArr3[i][j];
                    double y2 = dArr3[i + 1][j];
                    v[j] = (y2 - y1) / h;
                }
                return;
            }
        }
    }

    @Override // androidx.constraintlayout.core.motion.utils.CurveFit
    public double getSlope(double t, int j) {
        double t2;
        double[] dArr = this.f28mT;
        int n = dArr.length;
        if (t < dArr[0]) {
            t2 = dArr[0];
        } else if (t < dArr[n - 1]) {
            t2 = t;
        } else {
            t2 = dArr[n - 1];
        }
        for (int i = 0; i < n - 1; i++) {
            double[] dArr2 = this.f28mT;
            if (t2 <= dArr2[i + 1]) {
                double h = dArr2[i + 1] - dArr2[i];
                double d = (t2 - dArr2[i]) / h;
                double[][] dArr3 = this.f29mY;
                double y1 = dArr3[i][j];
                double y2 = dArr3[i + 1][j];
                return (y2 - y1) / h;
            }
        }
        return 0.0d;
    }

    @Override // androidx.constraintlayout.core.motion.utils.CurveFit
    public double[] getTimePoints() {
        return this.f28mT;
    }
}