SENTENCE_START = b"\x01"

SENTENCE_SYSTEM = b"\x11"
SENTENCE_VALID_PEERS = b"\x11\x20\x21"

TYPE_FANSPEED = b"\x29"[0]
TYPE_TEMP_OUTSIDE = b"\x32"[0]
TYPE_TEMP_EXHAUST = b"\x33"[0]
TYPE_TEMP_INSIDE = b"\x34"[0]
TYPE_TEMP_INCOMING = b"\x35"[0]

TEMP_IDENTIFIERS = dict(
    [
        (TYPE_TEMP_OUTSIDE, "TEMP_OUTSIDE"),
        (TYPE_TEMP_EXHAUST, "TEMP_EXHAUST"),
        (TYPE_TEMP_INSIDE, "TEMP_INSIDE"),
        (TYPE_TEMP_INCOMING, "TEMP_INCOMING"),
    ]
)

FANSPEED_LOOKUP = dict(
    [(1, 1), (3, 2), (7, 3), (15, 4), (31, 5), (63, 6), (127, 7), (255, 8)]
)

FANSPEED_SET = {
    "1": b"\x01\x11\x20\x29\x01\x5C\x01\x21\x10\x29\x01\x5C",
    "2": b"\x01\x11\x20\x29\x03\x5E\x01\x21\x10\x29\x03\x5E",
    "3": b"\x01\x11\x20\x29\x07\x62\x01\x21\x10\x29\x07\x62",
    "4": b"\x01\x11\x20\x29\x0F\x6A\x01\x21\x10\x29\x0F\x6A",
    "5": b"\x01\x11\x20\x29\x1F\x7A\x01\x21\x10\x29\x1F\x7A",
    "6": b"\x01\x11\x20\x29\x3F\x9A\x01\x21\x10\x29\x3F\x9A",
    "7": b"\x01\x11\x20\x29\x7F\xDA\x01\x21\x10\x29\x7F\xDA",
    "8": b"\x01\x11\x20\x29\xFF\x5A\x01\x21\x10\x29\xFF\x5A",
}

TEMP_LOOKUP = dict(
    [
        (0, -74),
        (1, -70),
        (2, -66),
        (3, -62),
        (4, -59),
        (5, -56),
        (6, -54),
        (7, -52),
        (8, -50),
        (9, -48),
        (10, -47),
        (11, -46),
        (12, -44),
        (13, -43),
        (14, -42),
        (15, -41),
        (16, -40),
        (17, -39),
        (18, -38),
        (19, -37),
        (20, -36),
        (21, -35),
        (22, -34),
        (23, -33),
        (24, -33),
        (25, -32),
        (26, -31),
        (27, -30),
        (28, -30),
        (29, -29),
        (30, -28),
        (31, -28),
        (32, -27),
        (33, -27),
        (34, -26),
        (35, -25),
        (36, -25),
        (37, -24),
        (38, -24),
        (39, -23),
        (40, -23),
        (41, -22),
        (42, -22),
        (43, -21),
        (44, -21),
        (45, -20),
        (46, -20),
        (47, -19),
        (48, -19),
        (49, -19),
        (50, -18),
        (51, -18),
        (52, -17),
        (53, -17),
        (54, -16),
        (55, -16),
        (56, -16),
        (57, -15),
        (58, -15),
        (59, -14),
        (60, -14),
        (61, -14),
        (62, -13),
        (63, -13),
        (64, -12),
        (65, -12),
        (66, -12),
        (67, -11),
        (68, -11),
        (69, -11),
        (70, -10),
        (71, -10),
        (72, -9),
        (73, -9),
        (74, -9),
        (75, -8),
        (76, -8),
        (77, -8),
        (78, -7),
        (79, -7),
        (80, -7),
        (81, -6),
        (82, -6),
        (83, -6),
        (84, -5),
        (85, -5),
        (86, -5),
        (87, -4),
        (88, -4),
        (89, -4),
        (90, -3),
        (91, -3),
        (92, -3),
        (93, -2),
        (94, -2),
        (95, -2),
        (96, -1),
        (97, -1),
        (98, -1),
        (99, -1),
        (100, 0),
        (101, 0),
        (102, 0),
        (103, 1),
        (104, 1),
        (105, 1),
        (106, 2),
        (107, 2),
        (108, 2),
        (109, 3),
        (110, 3),
        (111, 3),
        (112, 4),
        (113, 4),
        (114, 4),
        (115, 5),
        (116, 5),
        (117, 5),
        (118, 5),
        (119, 6),
        (120, 6),
        (121, 6),
        (122, 7),
        (123, 7),
        (124, 7),
        (125, 8),
        (126, 8),
        (127, 8),
        (128, 9),
        (129, 9),
        (130, 9),
        (131, 10),
        (132, 10),
        (133, 10),
        (134, 11),
        (135, 11),
        (136, 11),
        (137, 12),
        (138, 12),
        (139, 12),
        (140, 13),
        (141, 13),
        (142, 13),
        (143, 14),
        (144, 14),
        (145, 14),
        (146, 15),
        (147, 15),
        (148, 15),
        (149, 16),
        (150, 16),
        (151, 16),
        (152, 17),
        (153, 17),
        (154, 18),
        (155, 18),
        (156, 18),
        (157, 19),
        (158, 19),
        (159, 19),
        (160, 20),
        (161, 20),
        (162, 21),
        (163, 21),
        (164, 21),
        (165, 22),
        (166, 22),
        (167, 22),
        (168, 23),
        (169, 23),
        (170, 24),
        (171, 24),
        (172, 24),
        (173, 25),
        (174, 25),
        (175, 26),
        (176, 26),
        (177, 27),
        (178, 27),
        (179, 27),
        (180, 28),
        (181, 28),
        (182, 29),
        (183, 29),
        (184, 30),
        (185, 30),
        (186, 31),
        (187, 31),
        (188, 32),
        (189, 32),
        (190, 33),
        (191, 33),
        (192, 34),
        (193, 34),
        (194, 35),
        (195, 35),
        (196, 36),
        (197, 36),
        (198, 37),
        (199, 37),
        (200, 38),
        (201, 38),
        (202, 39),
        (203, 40),
        (204, 40),
        (205, 41),
        (206, 41),
        (207, 42),
        (208, 43),
        (209, 43),
        (210, 44),
        (211, 45),
        (212, 45),
        (213, 46),
        (214, 47),
        (215, 48),
        (216, 48),
        (217, 49),
        (218, 50),
        (219, 51),
        (220, 52),
        (221, 53),
        (222, 53),
        (223, 54),
        (224, 55),
        (225, 56),
        (226, 57),
        (227, 59),
        (228, 60),
        (229, 61),
        (230, 62),
        (231, 63),
        (232, 65),
        (233, 66),
        (234, 68),
        (235, 69),
        (236, 71),
        (237, 73),
        (238, 75),
        (239, 77),
        (240, 79),
        (241, 81),
        (242, 82),
        (243, 86),
        (244, 90),
        (245, 93),
        (246, 97),
        (247, 100),
        (248, 100),
        (249, 100),
        (250, 100),
        (251, 100),
        (252, 100),
        (253, 100),
        (254, 100),
        (255, 100),
    ]
)
