class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        sorted(arr)
        for i in range(len(arr)):
            if i == 0:
                arr[0] = 1
                continue
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
        return max(arr)

def main() -> None:
    s = Solution()
    arr = [1, 2, 2, 1, 2]
    print(s.maximumElementAfterDecrementingAndRearranging(arr))


if __name__ == "__main__":
    main()
