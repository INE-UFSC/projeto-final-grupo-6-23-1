LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY demux1_4 IS
PORT (
  f : IN std_logic;
  sel : IN std_logic_vector (1 DOWNTO 0);
  a, b, c, d : OUT std_logic
);
END demux1_4;

ARCHITECTURE arch OF demux1_4 IS
BEGIN
  process(f, sel)
  begin
    if(f='1') then
      case sel is
        when "00" =>
          a <= '1';
          b <= '0';
          c <= '0';
          d <= '0';
        when "01" =>
          a <= '0';
          b <= '1';
          c <= '0';
          d <= '0';
        when "10" =>
          a <= '0';
          b <= '0';
          c <= '1';
          d <= '0';
        when "11" =>
          a <= '0';
          b <= '0';
          c <= '0';
          d <= '1';
        when others =>
          a <= '0';
          b <= '0';
          c <= '0';
          d <= '0';
      end case;
    else
      a <= '0';
      b <= '0';
      c <= '0';
      d <= '0';
    end if;
  end process;
END arch;