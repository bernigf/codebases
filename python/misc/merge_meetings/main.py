"""

Programming exercise

Given an array that represents the meeting times of all AuditBoard employees, 
we want to return an array with all overlapping meeting times merged.
A meeting time is represented by a tuple i.e. (1, 3) where the value of the first element represents
the beginning of the meeting and the value of the second element represents the end of the meeting 

Example Array: [(1,4), (2,5), (7,10), (8, 12), (13, 15)]

Example return value: [(1,5), (7,12), (13,15)]

"""

def merge_meetings(all_meetings):
    
    # If no meetings, return empty list immediately
    if not all_meetings:
        return []

    # Sort meetings by their start time
    # This ensures overlapping meetings appear next to each other
    all_meetings.sort(key=lambda x: x[0])  # O(n log n)

    # Initialize merged list with the first meeting
    # This will act as our baseline comparison
    merged_meetings = [all_meetings[0]]
    remaining_meetings = all_meetings[1:]
    print(f"\nInitial remaining meetings: {remaining_meetings}")
    print(f"Initial merged list: {merged_meetings}\n")

    # Iterate through remaining meetings starting from second one
    for start, end in remaining_meetings:

        # Get the last merged meeting to compare overlap
        # Why the last one?
        #   Because AFTER SORTING the meetings (line 8), if overlap exists,
        #   it can ONLY happen with the most recently merged interval.
        last_start, last_end = merged_meetings[-1]
        print(f"Comparing:\nCurrent meeting {start, end}")
        print(f"To last merged meeting {last_start, last_end}\n")

        # Check if current meeting overlaps with last merged meeting
        # Overlap happens if current start is before or equal to last end
        if start <= last_end:

            # If overlapping:
            # - Start stays the same (last_start)
            # - End becomes the maximum of both ends
            #   because we want the merged interval to fully cover both
            merged_meetings[-1] = (last_start, max(last_end, end))
            print(f"MERGED (overlap) last merged meeting updated to {merged_meetings[-1]}\n")

        else:   
            
            # If no overlap:
            # This meeting is separate
            # Just append it to merged list
            merged_meetings.append((start, end))
            print(f"NEW (no overlap) meeting added to merged list: {merged_meetings[-1]}\n")

    # Return fully merged intervals
    return merged_meetings

# ---- Example Run ----
if __name__ == "__main__":

    all_meetings = [(1,4), (2,5), (7,10), (8, 12), (13, 15)]
    merged_meetings = merge_meetings(all_meetings)
    print(f"\nFinal merged meetings: {merged_meetings}\n")
