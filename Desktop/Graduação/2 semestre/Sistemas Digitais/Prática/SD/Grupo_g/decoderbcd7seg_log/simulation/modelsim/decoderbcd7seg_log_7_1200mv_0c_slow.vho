-- Copyright (C) 1991-2013 Altera Corporation
-- Your use of Altera Corporation's design tools, logic functions 
-- and other software and tools, and its AMPP partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Altera Program License 
-- Subscription Agreement, Altera MegaCore Function License 
-- Agreement, or other applicable license agreement, including, 
-- without limitation, that your use is for the sole purpose of 
-- programming logic devices manufactured by Altera and sold by 
-- Altera or its authorized distributors.  Please refer to the 
-- applicable agreement for further details.

-- VENDOR "Altera"
-- PROGRAM "Quartus II 64-Bit"
-- VERSION "Version 13.1.0 Build 162 10/23/2013 SJ Web Edition"

-- DATE "04/27/2023 12:44:26"

-- 
-- Device: Altera EP3C5E144C7 Package TQFP144
-- 

-- 
-- This VHDL file should be used for ModelSim-Altera (VHDL) only
-- 

LIBRARY CYCLONEIII;
LIBRARY IEEE;
USE CYCLONEIII.CYCLONEIII_COMPONENTS.ALL;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY 	decoderbcd7seg_log IS
    PORT (
	bcd : IN std_logic_vector(3 DOWNTO 0);
	a : BUFFER std_logic;
	b : BUFFER std_logic;
	c : BUFFER std_logic;
	d : BUFFER std_logic;
	e : BUFFER std_logic;
	f : BUFFER std_logic;
	g : BUFFER std_logic
	);
END decoderbcd7seg_log;

-- Design Ports Information
-- a	=>  Location: PIN_49,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- b	=>  Location: PIN_34,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- c	=>  Location: PIN_121,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- d	=>  Location: PIN_39,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- e	=>  Location: PIN_32,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- f	=>  Location: PIN_31,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- g	=>  Location: PIN_28,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- bcd[1]	=>  Location: PIN_1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- bcd[2]	=>  Location: PIN_30,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- bcd[3]	=>  Location: PIN_33,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- bcd[0]	=>  Location: PIN_44,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF decoderbcd7seg_log IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_bcd : std_logic_vector(3 DOWNTO 0);
SIGNAL ww_a : std_logic;
SIGNAL ww_b : std_logic;
SIGNAL ww_c : std_logic;
SIGNAL ww_d : std_logic;
SIGNAL ww_e : std_logic;
SIGNAL ww_f : std_logic;
SIGNAL ww_g : std_logic;
SIGNAL \a~output_o\ : std_logic;
SIGNAL \b~output_o\ : std_logic;
SIGNAL \c~output_o\ : std_logic;
SIGNAL \d~output_o\ : std_logic;
SIGNAL \e~output_o\ : std_logic;
SIGNAL \f~output_o\ : std_logic;
SIGNAL \g~output_o\ : std_logic;
SIGNAL \bcd[3]~input_o\ : std_logic;
SIGNAL \bcd[2]~input_o\ : std_logic;
SIGNAL \bcd[1]~input_o\ : std_logic;
SIGNAL \bcd[0]~input_o\ : std_logic;
SIGNAL \a~0_combout\ : std_logic;
SIGNAL \b~0_combout\ : std_logic;
SIGNAL \c~0_combout\ : std_logic;
SIGNAL \d~0_combout\ : std_logic;
SIGNAL \e~0_combout\ : std_logic;
SIGNAL \f~0_combout\ : std_logic;
SIGNAL \g~0_combout\ : std_logic;

BEGIN

ww_bcd <= bcd;
a <= ww_a;
b <= ww_b;
c <= ww_c;
d <= ww_d;
e <= ww_e;
f <= ww_f;
g <= ww_g;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;

-- Location: IOOBUF_X13_Y0_N16
\a~output\ : cycloneiii_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \a~0_combout\,
	devoe => ww_devoe,
	o => \a~output_o\);

-- Location: IOOBUF_X0_Y5_N16
\b~output\ : cycloneiii_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \b~0_combout\,
	devoe => ww_devoe,
	o => \b~output_o\);

-- Location: IOOBUF_X23_Y24_N16
\c~output\ : cycloneiii_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \c~0_combout\,
	devoe => ww_devoe,
	o => \c~output_o\);

-- Location: IOOBUF_X1_Y0_N16
\d~output\ : cycloneiii_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \d~0_combout\,
	devoe => ww_devoe,
	o => \d~output_o\);

-- Location: IOOBUF_X0_Y6_N16
\e~output\ : cycloneiii_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \e~0_combout\,
	devoe => ww_devoe,
	o => \e~output_o\);

-- Location: IOOBUF_X0_Y7_N2
\f~output\ : cycloneiii_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \f~0_combout\,
	devoe => ww_devoe,
	o => \f~output_o\);

-- Location: IOOBUF_X0_Y9_N9
\g~output\ : cycloneiii_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => \g~0_combout\,
	devoe => ww_devoe,
	o => \g~output_o\);

-- Location: IOIBUF_X0_Y6_N22
\bcd[3]~input\ : cycloneiii_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_bcd(3),
	o => \bcd[3]~input_o\);

-- Location: IOIBUF_X0_Y8_N15
\bcd[2]~input\ : cycloneiii_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_bcd(2),
	o => \bcd[2]~input_o\);

-- Location: IOIBUF_X0_Y23_N1
\bcd[1]~input\ : cycloneiii_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_bcd(1),
	o => \bcd[1]~input_o\);

-- Location: IOIBUF_X5_Y0_N15
\bcd[0]~input\ : cycloneiii_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_bcd(0),
	o => \bcd[0]~input_o\);

-- Location: LCCOMB_X1_Y4_N24
\a~0\ : cycloneiii_lcell_comb
-- Equation(s):
-- \a~0_combout\ = ((\bcd[2]~input_o\) # ((\bcd[1]~input_o\) # (!\bcd[0]~input_o\))) # (!\bcd[3]~input_o\)

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1111110111111111",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \bcd[3]~input_o\,
	datab => \bcd[2]~input_o\,
	datac => \bcd[1]~input_o\,
	datad => \bcd[0]~input_o\,
	combout => \a~0_combout\);

-- Location: LCCOMB_X1_Y4_N26
\b~0\ : cycloneiii_lcell_comb
-- Equation(s):
-- \b~0_combout\ = (\bcd[2]~input_o\ & ((!\bcd[0]~input_o\) # (!\bcd[1]~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0000110011001100",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	datab => \bcd[2]~input_o\,
	datac => \bcd[1]~input_o\,
	datad => \bcd[0]~input_o\,
	combout => \b~0_combout\);

-- Location: LCCOMB_X1_Y4_N4
\c~0\ : cycloneiii_lcell_comb
-- Equation(s):
-- \c~0_combout\ = (!\bcd[2]~input_o\ & (\bcd[1]~input_o\ & !\bcd[0]~input_o\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "0000000000110000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	datab => \bcd[2]~input_o\,
	datac => \bcd[1]~input_o\,
	datad => \bcd[0]~input_o\,
	combout => \c~0_combout\);

-- Location: LCCOMB_X1_Y4_N14
\d~0\ : cycloneiii_lcell_comb
-- Equation(s):
-- \d~0_combout\ = (\bcd[2]~input_o\ & ((\bcd[1]~input_o\ $ (!\bcd[0]~input_o\)))) # (!\bcd[2]~input_o\ & (!\bcd[3]~input_o\ & (!\bcd[1]~input_o\ & \bcd[0]~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1100000100001100",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \bcd[3]~input_o\,
	datab => \bcd[2]~input_o\,
	datac => \bcd[1]~input_o\,
	datad => \bcd[0]~input_o\,
	combout => \d~0_combout\);

-- Location: LCCOMB_X1_Y4_N16
\e~0\ : cycloneiii_lcell_comb
-- Equation(s):
-- \e~0_combout\ = (\bcd[0]~input_o\) # ((\bcd[2]~input_o\ & !\bcd[1]~input_o\))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1111111100001100",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	datab => \bcd[2]~input_o\,
	datac => \bcd[1]~input_o\,
	datad => \bcd[0]~input_o\,
	combout => \e~0_combout\);

-- Location: LCCOMB_X1_Y4_N10
\f~0\ : cycloneiii_lcell_comb
-- Equation(s):
-- \f~0_combout\ = (\bcd[2]~input_o\ & (((\bcd[1]~input_o\ & \bcd[0]~input_o\)))) # (!\bcd[2]~input_o\ & ((\bcd[1]~input_o\) # ((!\bcd[3]~input_o\ & \bcd[0]~input_o\))))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1111000100110000",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \bcd[3]~input_o\,
	datab => \bcd[2]~input_o\,
	datac => \bcd[1]~input_o\,
	datad => \bcd[0]~input_o\,
	combout => \f~0_combout\);

-- Location: LCCOMB_X1_Y4_N12
\g~0\ : cycloneiii_lcell_comb
-- Equation(s):
-- \g~0_combout\ = (\bcd[2]~input_o\ & (((\bcd[1]~input_o\ & \bcd[0]~input_o\)))) # (!\bcd[2]~input_o\ & (!\bcd[3]~input_o\ & (!\bcd[1]~input_o\)))

-- pragma translate_off
GENERIC MAP (
	lut_mask => "1100000100000001",
	sum_lutc_input => "datac")
-- pragma translate_on
PORT MAP (
	dataa => \bcd[3]~input_o\,
	datab => \bcd[2]~input_o\,
	datac => \bcd[1]~input_o\,
	datad => \bcd[0]~input_o\,
	combout => \g~0_combout\);

ww_a <= \a~output_o\;

ww_b <= \b~output_o\;

ww_c <= \c~output_o\;

ww_d <= \d~output_o\;

ww_e <= \e~output_o\;

ww_f <= \f~output_o\;

ww_g <= \g~output_o\;
END structure;


