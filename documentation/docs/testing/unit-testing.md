---
sidebar_position: 1
---
# Unit tests

## time_to_seconds 
Converts a time string to total seconds.

| Test Case | Input | Expected Result |
|---|---|---|
| MM:SS format | `"1:30"` | `90` |
| HH:MM:SS format | `"1:00:00"` | `3600` |
| Invalid string | `"bad"` | `0` |
| None input | `None` | `AttributeError` |
| Seconds only | `"45"` | `45` |
| Full HH:MM:SS | `"2:30:15"` | `9015` |

## normalize_text
Removes stopwords and map synonyms for a test string 
like the big dog  can just be big dog

| Test Case | Input | Expected Result |
|---|---|---|
| Removes stopwords | `"the big dog"` | `"big dog"` |
| Maps synonyms | `"scared"` | `"afraid"` |
| Empty string | `""` | `""` |

## build_segments_from_duration
Splits a video duration into timed segments for quiz question placement.

| Test Case | Input | Expected Result |
|---|---|---|
| Standard segments | `(180, 60)` | `[(0,59),(60,119),(120,179),(180,180)]` |
| Shorter last segment | `(90, 60)` | `[(0,59),(60,90)]` |
| Single segment | `(60, 60)` | `[(0,59),(60,60)]` |