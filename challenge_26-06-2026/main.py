class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        nums = [1 if i == target else -1 for i in nums]
        n = len(nums)
        tree_size = (2 * n) + 2
        tree = [0] * (tree_size + 1)
        def update(i, delta):
            while i <= tree_size:
                tree[i] += delta
                i += i & (-i)
        def query(i):
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & (-i)
            return total
        offset = n + 1
        update(0 + offset, 1)
        total_subarrays = 0
        current_psum = 0
        for num in nums:
            current_psum += num
            tree_idx = current_psum + offset
            total_subarrays += query(tree_idx - 1)
            update(tree_idx, 1)
        return total_subarrays


def main() -> None:
    raise NotImplentedError()


if __name__ == "__main__":
    main()
