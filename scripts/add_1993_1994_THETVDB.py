#!/usr/bin/env python3
"""
1993-1994 complete episodes from TheTVDB
Pushing toward 100% coverage of classic era
"""

import csv
from pathlib import Path

EPISODES_1993_1994 = [
    # 1993
    {'episode_id': 'HBB-1993-016', 'air_date': '1993-01-16', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Kyuss', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-023', 'air_date': '1993-01-23', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Dee Snider, Dave Mustaine', 'theme': 'Inaugural Ball', 'special_notes': 'Inaugural Ball with Dee Snider and Dave Mustaine', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-024', 'air_date': '1993-01-24', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Dave Mustaine', 'theme': '', 'special_notes': 'From Washington D.C. with Dave Mustaine', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-030', 'air_date': '1993-01-30', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Pro-Pain', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-037', 'air_date': '1993-02-06', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Al Jourgensen', 'theme': '', 'special_notes': 'Taped interview with Al Jourgensen', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-044', 'air_date': '1993-02-13', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Biohazard', 'theme': 'Countdown To The Ball', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-051', 'air_date': '1993-02-20', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Music Award Nominations Special', 'special_notes': 'Music Award Nominations Special', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-058', 'air_date': '1993-02-27', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Gruntruck, Rob Zombie', 'theme': '', 'special_notes': 'Gruntruck featured; Rob Zombie paints the set', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-065', 'air_date': '1993-03-06', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Flotsam & Jetsam, Rob Zombie', 'theme': '', 'special_notes': 'Flotsam & Jetsam; Rob Zombie painting', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-072', 'air_date': '1993-03-13', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Infectious Grooves', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-079', 'air_date': '1993-03-20', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': 'At Biker Week in Daytona Beach, FL', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-086', 'air_date': '1993-03-27', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Dream Theater, Green Jello', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-093', 'air_date': '1993-04-03', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Jackyl, Circus of Power', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-100', 'air_date': '1993-04-10', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Ugly Kid Joe, Animal Bag, Collision, Anthrax', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-107', 'air_date': '1993-04-17', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-114', 'air_date': '1993-04-24', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Living Colour, Sacred Reich', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-121', 'air_date': '1993-05-01', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Testament, Overkill, Rob Zombie', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-128', 'air_date': '1993-05-08', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Nuclear Assault, Quicksand, Rob Zombie', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-142', 'air_date': '1993-05-22', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax', 'theme': 'Trail of Noise - West Coast Part 1', 'special_notes': 'Trail of Noise with Anthrax West Coast Part 1', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-149', 'air_date': '1993-05-29', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax', 'theme': 'Trail of Noise - East Coast Part 2', 'special_notes': 'Trail of Noise with Anthrax East Coast Part 2', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-156', 'air_date': '1993-06-05', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Gene Simmons, Paul Stanley (Kiss)', 'theme': '', 'special_notes': 'With Gene Simmons and Paul Stanley of Kiss', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-163', 'air_date': '1993-06-12', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Butthole Surfers', 'theme': 'Birthday Show', 'special_notes': 'Riki Rachtman\'s Birth Day Show with Butthole Surfers', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-170', 'air_date': '1993-06-19', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Paw', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-177', 'air_date': '1993-06-26', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Raging Slab', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-184', 'air_date': '1993-07-03', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-191', 'air_date': '1993-07-10', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Blind Melon, Monster Magnet', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-198', 'air_date': '1993-07-17', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Vince Neil, Galactic Cowboys', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-205', 'air_date': '1993-07-24', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Lollapalooza \'93', 'special_notes': 'Host At Lollapalooza \'93', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-219', 'air_date': '1993-08-07', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'King Diamond, Mercyful Fate, Ozzy Osbourne', 'theme': '', 'special_notes': 'King Diamond and Mercyful Fate; Ozzy Osbourne special', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-226', 'air_date': '1993-08-14', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax, White Zombie, Quicksand', 'theme': 'On the Road', 'special_notes': 'On the Road in NY with Anthrax, White Zombie, and Quicksand', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-233', 'air_date': '1993-08-21', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Biohazard', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-240', 'air_date': '1993-08-28', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Steve Vai, Devin Townsend', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-247', 'air_date': '1993-09-04', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Metal Blocks', 'special_notes': 'Metal Blocks Edition', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-254', 'air_date': '1993-09-11', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Morbid Angel', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-261', 'air_date': '1993-09-18', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Foundation Forum Show \'93', 'special_notes': 'Foundation Forum Show \'93', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-268', 'air_date': '1993-09-25', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Gary Hoey, Rob Halford, Slayer', 'theme': 'Ball-B-Q Part 2', 'special_notes': 'Riki Rachtman\'s Ball-B-Q Part 2', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-275', 'air_date': '1993-10-02', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'My Little Funhouse', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-282', 'air_date': '1993-10-09', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Duff McKagan', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-289', 'air_date': '1993-10-16', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Cathedral', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-296', 'air_date': '1993-10-23', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'I Mother Earth', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-303', 'air_date': '1993-10-30', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Danzig, Motorhead', 'theme': 'Halloween Special', 'special_notes': 'Halloween Special', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-310', 'air_date': '1993-11-06', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'My Sister\'s Machine', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-317', 'air_date': '1993-11-13', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Skid Row', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-324', 'air_date': '1993-11-20', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'The Melvins', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-331', 'air_date': '1993-11-27', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Fight, Fudge Tunnel', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-338', 'air_date': '1993-12-04', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-345', 'air_date': '1993-12-11', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Lars Ulrich (Metallica)', 'theme': '', 'special_notes': 'With Lars Ulrich of Metallica', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1993-352', 'air_date': '1993-12-18', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Metallica', 'theme': 'Sh*t, Binge & Purge Special', 'special_notes': 'Metallica Live; Sh*t, Binge & Purge Special', 'source_citations': 'thetvdb.com'},

    # 1994
    {'episode_id': 'HBB-1994-001', 'air_date': '1994-01-01', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Best of 1993', 'special_notes': 'Best of 1993', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-008', 'air_date': '1994-01-08', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-015', 'air_date': '1994-01-15', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax', 'theme': 'Trail of Noise', 'special_notes': 'Trail of Noise with Anthrax', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-022', 'air_date': '1994-01-22', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Prong', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-029', 'air_date': '1994-01-29', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Bad Religion', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-036', 'air_date': '1994-02-05', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'NHL All-Star Game (pre-empted)', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-043', 'air_date': '1994-02-12', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': 'Riki Rachtman Hosts From Alcatraz', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-050', 'air_date': '1994-02-19', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Metallica', 'theme': '', 'special_notes': 'With Metallica in San Francisco', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-057', 'air_date': '1994-02-26', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Pantera', 'theme': '', 'special_notes': 'With studio reports from Pantera', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-064', 'air_date': '1994-03-05', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Mutha\'s Day Out', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-071', 'air_date': '1994-03-12', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Soundgarden', 'theme': '', 'special_notes': 'With Soundgarden in Seattle', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-085', 'air_date': '1994-03-26', 'episode_number': '', 'season': '1993-1994', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Pantera', 'theme': '', 'special_notes': 'With Pantera in Dallas, Texas', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-092', 'air_date': '1994-04-02', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-099', 'air_date': '1994-04-09', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Pre-empted by MTV News coverage of Kurt Cobain\'s death', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-106', 'air_date': '1994-04-16', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'King\'s X', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-113', 'air_date': '1994-04-23', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Metal Blox', 'special_notes': 'Metal Blox Edition', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-120', 'air_date': '1994-04-30', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Zakk Wylde', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-127', 'air_date': '1994-05-07', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-134', 'air_date': '1994-05-14', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Henry Rollins', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-141', 'air_date': '1994-05-21', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-148', 'air_date': '1994-05-28', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Memorial Day Weekend', 'special_notes': 'Memorial Day Weekend with mostly Bar-B-Que \'93 repeat clips', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-155', 'air_date': '1994-06-04', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-162', 'air_date': '1994-06-11', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'GWAR, Infectious Grooves', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-169', 'air_date': '1994-06-18', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Biohazard', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-176', 'air_date': '1994-06-25', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Gene Simmons (Kiss)', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-183', 'air_date': '1994-07-02', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Soundgarden', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-190', 'air_date': '1994-07-09', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Alice Cooper', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-197', 'air_date': '1994-07-16', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Motley Crue', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-204', 'air_date': '1994-07-23', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Stuttering John, Sugar Tooth', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-211', 'air_date': '1994-07-30', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Bruce Dickinson', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-218', 'air_date': '1994-08-06', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Ozzy Osbourne', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-221', 'air_date': '1994-08-09', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Movie Premier Of Airheads', 'special_notes': 'Movie Premier Of Airheads - one-hour special', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-225', 'air_date': '1994-08-13', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Woodstock \'94', 'special_notes': 'Woodstock \'94', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-232', 'air_date': '1994-08-20', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': 'Host From Alcatraz', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-239', 'air_date': '1994-08-27', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'House of Pain', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-246', 'air_date': '1994-09-03', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Video Music Awards Nominees', 'special_notes': 'Video Music Awards Nominees', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-253', 'air_date': '1994-09-10', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Metallica', 'theme': '', 'special_notes': 'Metallica in San Francisco', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-260', 'air_date': '1994-09-17', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Pre-empted by Beavis & Butthead Marathon', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-267', 'air_date': '1994-09-24', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Metal Blox', 'special_notes': 'Metal Blox Edition', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-274', 'air_date': '1994-10-01', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-281', 'air_date': '1994-10-08', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Gilby Clarke', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-288', 'air_date': '1994-10-15', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Queensryche', 'theme': 'Promise Land Listening Party', 'special_notes': 'Queensryche Promise Land Listening Party', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-295', 'air_date': '1994-10-22', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Dream Theater', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-302', 'air_date': '1994-10-29', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Megadeth, Slayer', 'theme': 'Halloween Special', 'special_notes': 'Night of the Living Megadeth; Halloween Special with Slayer', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-309', 'air_date': '1994-11-05', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-316', 'air_date': '1994-11-12', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Corrosion of Conformity', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-323', 'air_date': '1994-11-19', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Type O Negative', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-330', 'air_date': '1994-11-26', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': '', 'guest_host': '', 'theme': '', 'special_notes': 'Pre-empted by Beavis & Butthead', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-337', 'air_date': '1994-12-03', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Rancid', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-344', 'air_date': '1994-12-10', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Marilyn Manson', 'theme': '', 'special_notes': 'At Woodstock \'94 with Marilyn Manson', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-351', 'air_date': '1994-12-17', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Best of 1994', 'special_notes': 'Best of 1994', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-358', 'air_date': '1994-12-24', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1994-365', 'air_date': '1994-12-31', 'episode_number': '', 'season': '1994-1995', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
]

def add_episodes(episodes_list):
    """Add episodes."""
    data_dir = Path('data')
    episodes_file = data_dir / 'episodes.csv'

    existing_ids = set()
    if episodes_file.exists():
        with open(episodes_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_ids = {row['episode_id'] for row in reader if row.get('episode_id')}

    new_to_add = [ep for ep in episodes_list if ep['episode_id'] not in existing_ids]

    if not new_to_add:
        return 0

    with open(episodes_file, 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['episode_id', 'air_date', 'episode_number', 'season', 'era',
                      'host', 'guest_host', 'theme', 'special_notes', 'source_citations']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for ep in new_to_add:
            writer.writerow(ep)

    return len(new_to_add)

if __name__ == "__main__":
    count = add_episodes(EPISODES_1993_1994)
    print(f"✅ Added {count} episodes from TheTVDB!")
    print(f"🎸 1993-1994 EXPLODING!")
    print(f"📺 Classic era completion imminent!")
