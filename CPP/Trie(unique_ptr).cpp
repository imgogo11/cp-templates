struct Node {
    unique_ptr<Node> child[26];
    bool end = false;
};

class Trie {
  private:
    Node root;

  public:
    Trie() {}

    void insert(string word) {
        auto p = &root;
        for (char c : word) {
            int idx = c - 'a';
            if (!p->child[idx]) {
                p->child[idx] = make_unique<Node>();
            }
            p = p->child[idx].get();
        }
        p->end = true;
    }

    bool search(string word) {
        auto p = &root;
        for (char c : word) {
            int idx = c - 'a';
            if (!p->child[idx]) {
                return false;
            }
            p = p->child[idx].get();
        }
        return p->end;
    }

    bool startsWith(string prefix) {
        auto p = &root;
        for (char c : prefix) {
            int idx = c - 'a';
            if (!p->child[idx]) {
                return false;
            }
            p = p->child[idx].get();
        }
        return true;
    }
};
