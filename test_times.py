from times import compute_overlap_time,time_range
import pytest

def test_given_input():
    if __name__ == "__main__":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
        result = compute_overlap_time(large,short)
        expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
        assert result == expected

def test_no_overlap():
    if __name__ == "__main__":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 10:15:00")
        short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
        result1 = compute_overlap_time(large,short)
        assert all(x > y for x,y in result1)

def test_sev_intervals():
    if __name__ == "__main__":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",2,60)
        short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
        result = compute_overlap_time(large,short)
        expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
        assert result == expected

def test_end_equals_start():
    if __name__ == "__main__":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",2,60)
        short = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00", 2, 60)
        result = compute_overlap_time(large,short)
        assert all(x > y for x,y in result)

def test_backwards():
    if __name__ == "__main__":
        with pytest.raises(ValueError, match="End time is less than start time"):
            time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00", 2, 60)
