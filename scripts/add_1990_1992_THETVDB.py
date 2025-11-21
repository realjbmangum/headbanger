#!/usr/bin/env python3
"""
1990-1992 episodes from TheTVDB complete listing
Filling gaps to reach 52 episodes per year
"""

import csv
from pathlib import Path

EPISODES_1990_1992 = [
    # 1990 - Missing episodes
    {'episode_id': 'HBB-1990-034', 'air_date': '1990-02-03', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Gothic Slam, Britny Fox, Slaughter', 'theme': '', 'special_notes': 'Appearances by Gothic Slam, Britny Fox & Slaughter', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-041', 'air_date': '1990-02-10', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Great White, Havana Black', 'theme': '', 'special_notes': 'Taped interviews with Great White & Havana Black', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-048', 'air_date': '1990-02-17', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-055', 'air_date': '1990-02-24', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Babylon A.D., D.R.I.', 'theme': '', 'special_notes': 'Featured Babylon A.D. and D.R.I.', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-069', 'air_date': '1990-03-10', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'XYZ, Icon', 'theme': '', 'special_notes': 'XYZ & Icon performances', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-076', 'air_date': '1990-03-17', 'episode_number': '', 'season': '1989-1990', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Bad Brains', 'theme': '', 'special_notes': 'Bad Brains episode', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-118', 'air_date': '1990-04-28', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Mike Muir (Suicidal Tendencies), Taime Downe', 'theme': '', 'special_notes': 'Phone interviews with Mike Muir & Taime Downe', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-153', 'air_date': '1990-06-02', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Lita Ford', 'guest_host': '', 'theme': '', 'special_notes': 'Lita Ford hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-174', 'air_date': '1990-06-23', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Poison', 'guest_host': '', 'theme': '', 'special_notes': 'Poison hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-181', 'air_date': '1990-06-30', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Death Angel', 'guest_host': '', 'theme': '', 'special_notes': 'Death Angel hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-202', 'air_date': '1990-07-21', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Faith No More', 'theme': 'On the Road', 'special_notes': 'On the Road with Faith No More', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-216', 'air_date': '1990-08-04', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Bruce Dickinson', 'guest_host': '', 'theme': '', 'special_notes': 'Bruce Dickinson of Iron Maiden hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-223', 'air_date': '1990-08-11', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Dave Mustaine, David Ellefson', 'guest_host': '', 'theme': '', 'special_notes': 'Dave Mustaine & David Ellefson of Megadeth hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-230', 'air_date': '1990-08-18', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Anthrax', 'theme': '', 'special_notes': 'Anthrax with Megaforce office road reports', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-237', 'air_date': '1990-08-25', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Vixen', 'theme': 'Rock Blocks', 'special_notes': 'Vixen Album Party Rock Blocks Edition', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-243', 'air_date': '1990-08-31', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Poison', 'theme': '', 'special_notes': 'Poison Festival of the Flesh Contest', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-251', 'air_date': '1990-09-08', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Poison', 'theme': '', 'special_notes': 'Poison Festival of the Flesh At Castle Donnington Part II', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-258', 'air_date': '1990-09-15', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Ratt, Stryper, Doro Pesch', 'theme': '', 'special_notes': 'Ratt, Stryper & Doro Pesch featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-272', 'air_date': '1990-09-29', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Michael Wilton, Chris DeGarmo (Queensryche)', 'theme': '', 'special_notes': 'Michael Wilton & Chris DeGarmo of Queensryche', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-279', 'air_date': '1990-10-06', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Living Colour', 'guest_host': '', 'theme': '', 'special_notes': 'Living Colour hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-293', 'air_date': '1990-10-20', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'The Scorpions', 'theme': '', 'special_notes': 'The Scorpions featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-321', 'air_date': '1990-11-17', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Winger', 'guest_host': '', 'theme': '', 'special_notes': 'Winger hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-342', 'air_date': '1990-12-08', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Suicidal Tendencies', 'theme': 'On the Road', 'special_notes': 'Road Report From Suicidal Tendencies', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-350', 'air_date': '1990-12-16', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Jani Lane', 'theme': '', 'special_notes': 'Monsters Of Rock Sunday, RIP Magazine 4th Anniversary Party & Year End Top 20 Metal Countdown With Jani Lane', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1990-356', 'air_date': '1990-12-22', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Vince Neil, Tommy Lee', 'theme': 'Decade of Metal Countdown', 'special_notes': 'Decade of Metal Countdown With Vince Neil & Tommy Lee', 'source_citations': 'thetvdb.com'},

    # 1991 - Missing episodes
    {'episode_id': 'HBB-1991-005', 'air_date': '1991-01-05', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Trixter', 'guest_host': '', 'theme': '', 'special_notes': 'Trixter hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-012', 'air_date': '1991-01-12', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman, Jani Lane', 'guest_host': '', 'theme': 'Top 20 Year End Countdown', 'special_notes': 'Riki Rachtman & Jani Lane Host Top 20 Year End Countdown', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-054', 'air_date': '1991-02-23', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Metal Blox', 'special_notes': 'Metal Blox Edition', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-061', 'air_date': '1991-03-02', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Alice In Chains, Lynch Mob', 'theme': '', 'special_notes': 'KNAC 5th Anniversary Benefit Show With Alice In Chains, Lynch Mob & Others', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-068', 'air_date': '1991-03-09', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'The Throbs', 'theme': '', 'special_notes': 'The Throbs featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-075', 'air_date': '1991-03-16', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Cinderella', 'guest_host': '', 'theme': '', 'special_notes': 'Cinderella hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-082', 'air_date': '1991-03-23', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'The Bulletboys', 'guest_host': '', 'theme': '', 'special_notes': 'The Bulletboys hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-089', 'air_date': '1991-03-30', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Metal Blox', 'special_notes': 'Metal Blox Edition', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-103', 'air_date': '1991-04-13', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Pantera, Alice In Chains', 'theme': '', 'special_notes': 'Pantera & Alice In Chains featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-110', 'air_date': '1991-04-20', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'White Lion, Mind Funk', 'theme': '', 'special_notes': 'White Lion & Mind Funk', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-117', 'air_date': '1991-04-27', 'episode_number': '', 'season': '1990-1991', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Mr. Big, Kreator', 'theme': '', 'special_notes': 'Mr. Big & Kreator', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-124', 'air_date': '1991-05-04', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Lemmy Kilmister', 'guest_host': '', 'theme': '', 'special_notes': 'Lemmy Kilmister of Motorhead hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-145', 'air_date': '1991-05-25', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Megadeth', 'theme': 'Rock Blocks', 'special_notes': 'Mission Megadeth At the Cat House Part 2 Rock Blocks Edition', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-159', 'air_date': '1991-06-08', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Cycle Sluts From Hell, Junkyard', 'theme': '', 'special_notes': 'Cycle Sluts From Hell & Junkyard Album Release Party', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-173', 'air_date': '1991-06-22', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Armored Saint, Suicidal Tendencies', 'theme': '', 'special_notes': 'Armored Saint & Suicidal Tendencies', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-187', 'air_date': '1991-07-06', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Slayer', 'theme': 'On the Road', 'special_notes': 'On the Road With Slayer In New York', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-194', 'air_date': '1991-07-13', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Megadeth, Slayer, Anthrax, Chuck D., Alice In Chains', 'theme': 'Clash of the Titans', 'special_notes': 'Clash of the Titans With Megadeth, Slayer, Anthrax, Chuck D., & Alice In Chains', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-215', 'air_date': '1991-08-03', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Aldo Nova', 'guest_host': '', 'theme': '', 'special_notes': 'Aldo Nova hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-222', 'air_date': '1991-08-10', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'L.A. Guns', 'guest_host': '', 'theme': '', 'special_notes': 'L.A. Guns hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-236', 'air_date': '1991-08-24', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Bang Tango, Liquid Jesus', 'theme': '', 'special_notes': 'Bang Tango & Liquid Jesus', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-243', 'air_date': '1991-08-31', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Megadeth', 'guest_host': '', 'theme': '', 'special_notes': 'Megadeth hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-250', 'air_date': '1991-09-07', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Queensryche', 'theme': 'Invading the Empire', 'special_notes': 'Invading the Empire With Queensryche In London Part 1', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-257', 'air_date': '1991-09-14', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Monsters Of Rock', 'special_notes': 'Invading the Empire At Monsters Of Rock Part 2', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-271', 'air_date': '1991-09-28', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Pearl Jam', 'theme': '', 'special_notes': 'Pearl Jam featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-278', 'air_date': '1991-10-05', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'XYZ, The Cult', 'theme': '', 'special_notes': 'XYZ & The Cult', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-313', 'air_date': '1991-11-09', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Ugly Kid Joe, Law & Order, Infectious Grooves', 'theme': '', 'special_notes': 'Ugly Kid Joe, Law & Order, & Infectious Grooves', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-320', 'air_date': '1991-11-16', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Fates Warning', 'theme': '', 'special_notes': 'Fates Warning featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-334', 'air_date': '1991-11-30', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Prong, Soundgarden, Corrosion Of Conformity', 'theme': '', 'special_notes': 'Prong, Soundgarden, Corrosion Of Conformity', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1991-362', 'air_date': '1991-12-28', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Rock In Rio', 'special_notes': 'Encore of Rock In Rio Pt. 1 & 2', 'source_citations': 'thetvdb.com'},

    # 1992 - Missing episodes
    {'episode_id': 'HBB-1992-011', 'air_date': '1992-01-11', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Best Of 91', 'special_notes': 'Best Of 91', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-025', 'air_date': '1992-01-25', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Primus', 'theme': 'Metal Blocks', 'special_notes': 'Primus At the Cat House Metal Blocks Edition', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-032', 'air_date': '1992-02-01', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Ozzy Osbourne, Prong', 'theme': 'On the Road', 'special_notes': 'On the Road With Ozzy Osbourne & Prong', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-039', 'air_date': '1992-02-08', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Scatterbrain, Ugly Kid Joe', 'theme': '', 'special_notes': 'Scatterbrain & Ugly Kid Joe At the Scrap Bar', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-060', 'air_date': '1992-02-29', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'L.A. Guns', 'theme': '', 'special_notes': 'L.A. Guns featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-067', 'air_date': '1992-03-07', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'My Sister\'s Machine, Overkill', 'theme': 'Countdown To The Ball', 'special_notes': 'My Sister\'s Machine & Overkill (New Set & Countdown To The Ball)', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-074', 'air_date': '1992-03-14', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Skid Row, Pantera', 'theme': 'On the Road', 'special_notes': 'On the Road With Skid Row & Pantera Part 2', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-088', 'air_date': '1992-03-28', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Spinal Tap', 'guest_host': '', 'theme': '', 'special_notes': 'Spinal Tap hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-095', 'air_date': '1992-04-04', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Roxy Blue, Motorpsycho', 'theme': '', 'special_notes': 'Roxy Blue & Motorpsycho', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-102', 'air_date': '1992-04-11', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Blackie Lawless, Vanessa Warwick', 'theme': '', 'special_notes': 'Iron Maiden Release Party With Blackie Lawless & Vanessa Warwick', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-109', 'air_date': '1992-04-18', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Slaughter', 'theme': '', 'special_notes': 'Slaughter featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-116', 'air_date': '1992-04-25', 'episode_number': '', 'season': '1991-1992', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Slik Toxik, White Zombie, King\'s X, Corrosion of Conformity', 'theme': '', 'special_notes': 'Slik Toxik, White Zombie, King\'s X, & Corrosion of Conformity', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-132', 'air_date': '1992-05-12', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Megadeth', 'theme': '', 'special_notes': 'Repeat of Megadeth Show', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-144', 'air_date': '1992-05-23', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Testament, Shotgun Messiah', 'theme': '', 'special_notes': 'Testament & Shotgun Messiah', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-151', 'air_date': '1992-05-30', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Prong', 'theme': '', 'special_notes': 'Prong featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-158', 'air_date': '1992-06-06', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': 'No Guest', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-165', 'air_date': '1992-06-13', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Tora Tora, Saigon Kick, Suicidal Tendencies', 'theme': '', 'special_notes': 'Tora Tora, Saigon Kick & Suicidal Tendencies', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-179', 'air_date': '1992-06-27', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Iron Maiden', 'guest_host': '', 'theme': '', 'special_notes': 'Iron Maiden hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-186', 'air_date': '1992-07-04', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Metal Blox', 'special_notes': 'Metal Blox Edition', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-193', 'air_date': '1992-07-11', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': '', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-200', 'air_date': '1992-07-18', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Faith No More', 'guest_host': '', 'theme': '', 'special_notes': 'Faith No More hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-207', 'air_date': '1992-07-25', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Ugly Kid Joe', 'guest_host': '', 'theme': '', 'special_notes': 'Ugly Kid Joe hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-214', 'air_date': '1992-08-01', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Kiss', 'guest_host': '', 'theme': '', 'special_notes': 'Kiss hosted', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-221', 'air_date': '1992-08-08', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Joe Satriani, T-Ride', 'theme': '', 'special_notes': 'Joe Satriani & T-Ride', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-228', 'air_date': '1992-08-15', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Danzig, Black Sabbath', 'theme': '', 'special_notes': 'Danzig & Black Sabbath', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-242', 'air_date': '1992-08-29', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Alice In Chains', 'theme': '', 'special_notes': 'Alice In Chains At Mansion', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-256', 'air_date': '1992-09-12', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'White Zombie, Pantera', 'theme': '', 'special_notes': 'White Zombie & Pantera', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-263', 'air_date': '1992-09-19', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': '', 'special_notes': 'No Guest', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-270', 'air_date': '1992-09-26', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Mike Muir (Suicidal Tendencies)', 'theme': '', 'special_notes': 'Mike Muir Of Suicidal Tendencies', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-291', 'air_date': '1992-10-17', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'AC/DC', 'theme': '', 'special_notes': 'AC/DC', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-298', 'air_date': '1992-10-24', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Faster Pussycat, Bad4Good', 'theme': '', 'special_notes': 'Faster Pussycat & Bad4Good', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-319', 'air_date': '1992-11-14', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Alice In Chains', 'theme': '', 'special_notes': 'Alice In Chains In New Orleans', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-326', 'air_date': '1992-11-21', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Exodus', 'theme': '', 'special_notes': 'Exodus featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-333', 'air_date': '1992-11-28', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'The Ramones', 'theme': '', 'special_notes': 'The Ramones featured', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-347', 'air_date': '1992-12-12', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': 'Brian Johnson (AC/DC), Bad Biscuit', 'theme': '', 'special_notes': 'Brian Johnson of AC/DC & Bad Biscuit In New York', 'source_citations': 'thetvdb.com'},
    {'episode_id': 'HBB-1992-353', 'air_date': '1992-12-19', 'episode_number': '', 'season': '1992-1993', 'era': 'Classic MTV', 'host': 'Riki Rachtman', 'guest_host': '', 'theme': 'Best of 1992', 'special_notes': 'Best of 1992', 'source_citations': 'thetvdb.com'},
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
    count = add_episodes(EPISODES_1990_1992)
    print(f"✅ Added {count} episodes from TheTVDB!")
    print(f"🎸 Filling 1990-1992 gaps!")
    print(f"📺 Pushing toward 90%+ coverage!")
