class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str
    ) -> int:

        prefix = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

        def to_day(date: str) -> int:
            month = int(date[:2])
            day = int(date[3:])
            return prefix[month - 1] + day

        alice_start = to_day(arriveAlice)
        alice_end = to_day(leaveAlice)
        bob_start = to_day(arriveBob)
        bob_end = to_day(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        return max(0, end - start + 1)