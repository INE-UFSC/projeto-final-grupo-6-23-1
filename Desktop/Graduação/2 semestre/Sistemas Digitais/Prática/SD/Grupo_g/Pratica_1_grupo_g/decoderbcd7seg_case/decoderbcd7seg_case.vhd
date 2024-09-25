library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity decoderbcd7seg_case is
    port (
        bcd : in std_logic_vector(3 downto 0);
        abcdefg : out std_logic_vector(6 downto 0)
    );
end entity;

architecture arch of decoderbcd7seg_case is
begin

    process(bcd) is
    begin
        case bcd is
            when "0000" =>  -- 0
                abcdefg <= "1111110";
            when "0001" =>  -- 1
                abcdefg <= "0110000";
            when "0010" =>  -- 2
                abcdefg <= "1101101";
            when "0011" =>  -- 3
                abcdefg <= "1111001";
            when "0100" =>  -- 4
                abcdefg <= "0110011";
            when "0101" =>  -- 5
                abcdefg <= "1011011";
            when "0110" =>  -- 6
                abcdefg <= "1011111";
            when "0111" =>  -- 7
                abcdefg <= "1110000";
            when "1000" =>  -- 8
                abcdefg <= "1111111";
            when "1001" =>  -- 9
                abcdefg <= "1110011";
            when others =>  -- others
                abcdefg <= "0000000";
        end case;
    end process;

end architecture;

