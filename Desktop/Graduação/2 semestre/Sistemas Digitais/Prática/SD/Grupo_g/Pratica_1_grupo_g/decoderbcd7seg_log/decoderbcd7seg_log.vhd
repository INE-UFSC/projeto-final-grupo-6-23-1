LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY decoderbcd7seg_log IS
PORT (
bcd : IN std_logic_vector(3 DOWNTO 0);
a, b, c, d, e, f, g : OUT std_logic
);
END decoderbcd7seg_log;

ARCHITECTURE arch OF decoderbcd7seg_log IS


BEGIN

A <= (bcd(2) and not(bcd(1)) and not(bcd(0))) or (not(bcd(3) and not(bcd(2)) and not(bcd(1)) and bcd(0)) or (bcd(2) and not(bcd(1)) and not(bcd(1)) and bcd(0)));
B <= (bcd(2) and not(bcd(1) and bcd(0))) or (bcd(2) and bcd(1) and not(bcd(0)));
C <= (not(bcd(2)) and bcd(1) and not(bcd(0)));
D <= (bcd(2) and not(bcd(1)) and not(bcd(0))) or (not(bcd(3)) and not(bcd(2)) and not(bcd(1)) and bcd(0)) or ((bcd(2) and bcd(1) and bcd(0)));
E <= (bcd(2) and not(bcd(1))) or (bcd(0));
F <= (bcd(1) and bcd(0)) or ((not(bcd(3)) and not(bcd(2)) and not(bcd(1)) and bcd(0)) or (not(bcd(2)) and bcd(1)));
G <= (not(bcd(3)) and not(bcd(2)) and not(bcd(1))) or (bcd(2) and bcd(1) and bcd(0));

END ARCHITECTURE;