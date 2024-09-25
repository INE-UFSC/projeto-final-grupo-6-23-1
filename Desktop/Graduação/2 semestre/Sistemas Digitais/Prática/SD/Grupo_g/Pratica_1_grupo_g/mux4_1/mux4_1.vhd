LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY mux4_1 IS
GENERIC (N : POSITIVE := 1);
PORT (
a, b, c, d : IN std_logic_vector (N-1 DOWNTO 0);
sel : IN std_logic_vector (1 DOWNTO 0);
y : OUT std_logic_vector (N - 1 DOWNTO 0)
);
END mux4_1;

ARCHITECTURE arch OF mux4_1 IS

BEGIN

with sel select
y <=
	a when "00",
	b when "01",
	c when "10",
	d when others;


END arch;
