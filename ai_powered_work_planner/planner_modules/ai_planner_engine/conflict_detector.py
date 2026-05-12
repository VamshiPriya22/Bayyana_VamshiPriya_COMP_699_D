from planner_modules.schedule_management.models import Shift


class ConflictDetector:

    @staticmethod
    def detect_conflicts(shifts):
        print("🔍 Checking conflicts...")

        # 🔥 SORT SHIFTS FIRST (VERY IMPORTANT)
        shifts = sorted(shifts, key=lambda x: x.start_time)

        conflicts = []

        for i in range(len(shifts)):
            for j in range(i + 1, len(shifts)):
                s1 = shifts[i]
                s2 = shifts[j]

                # 🔥 SKIP INVALID DATA
                if s1.end_time <= s1.start_time or s2.end_time <= s2.start_time:
                    print("⚠ Invalid shift detected, skipping")
                    continue

                print(f"Comparing: {s1.start_time} - {s1.end_time}  WITH  {s2.start_time} - {s2.end_time}")

                # 🔥 CORRECT OVERLAP CONDITION
                if s1.start_time < s2.end_time and s2.start_time < s1.end_time:
                    print("❗ Conflict Found")
                    conflicts.append((s1, s2))

        print("✅ Total conflicts:", len(conflicts))
        return conflicts

    @staticmethod
    def count_conflicts(shifts):
        return len(ConflictDetector.detect_conflicts(shifts))

    @staticmethod
    def calculate_gaps(shifts):
        print("📏 Calculating gaps...")

        # 🔥 SORT SHIFTS
        sorted_shifts = sorted(shifts, key=lambda x: x.start_time)
        gaps = []

        for i in range(len(sorted_shifts) - 1):
            current_shift = sorted_shifts[i]
            next_shift = sorted_shifts[i + 1]

            # 🔥 VALIDATION
            if current_shift.end_time <= current_shift.start_time:
                continue

            gap_hours = (next_shift.start_time - current_shift.end_time).total_seconds() / 3600

            print(f"Gap between shift {i} and {i+1}: {gap_hours} hours")

            gaps.append(gap_hours)

        return gaps