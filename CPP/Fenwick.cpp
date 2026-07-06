template <typename T>
struct Fenwick {
    int n_;
    std::vector<T> a;
    Fenwick(int n = 0) {
        init(n);
    }
    void init(int n) {
        n_ = n;
        a.assign(n, T{});
    }
    void add(int x, const T &v) {
        for (int i = x + 1; i <= n_; i += i & -i) {
            a[i - 1] = a[i - 1] + v;
        }
    }
    T sum(int x) {  // [0,x)
        T ans{};
        for (int i = x; i > 0; i -= i & -i) {
            ans = ans + a[i - 1];
        }
        return ans;
    }
    T rangeSum(int l, int r) {  // [l,r)
        return sum(r) - sum(l);
    }
    int select(const T &k) {  // 返回最大的 x，使得 sum[0,x) <= k
        int x = 0;
        T cur{};
        for (int i = 1 << std::__lg(n_); i; i /= 2) {
            if (x + i <= n_ && cur + a[x + i - 1] <= k) {
                x += i;
                cur = cur + a[x - 1];
            }
        }
        return x;
    }
};