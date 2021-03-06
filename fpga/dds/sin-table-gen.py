import math
addr_bits = 12
data_bits = 12

def to_bin(x, n):
    return ('{0:0' + str(n) + 'b}').format(x)[-n:]

with open("dds-sine-table.gen.vhd", 'w') as f:
    f.write("--Autogenerated sine table - do not modify\n")
    f.write("library IEEE;\n")
    f.write("use IEEE.STD_LOGIC_1164.ALL;\n")
    f.write("use IEEE.NUMERIC_STD.ALL;\n\n")
    f.write("entity dds_sine_table is\n")
    f.write("\tport(\n")
    f.write("\t\tclock : in std_logic;\n")
    f.write("\t\taddress : in std_logic_vector(" + str(addr_bits - 1) + " downto 0);\n")
    f.write("\t\tdata : out std_logic_vector(" + str(data_bits - 1) + " downto 0));\n")
    f.write("end dds_sine_table;\n\n")
    f.write("architecture Behavioral of dds_sine_table is\n")
    f.write("begin\n")
    f.write("\tprocess(clock)\n")
    f.write("\tbegin\n")
    f.write("\t\tif rising_edge(clock) then\n")
    f.write("\t\t\tcase address is\n")
    for x in range(0, 2**addr_bits):
        val = math.sin(2.0 * math.pi * (x / float(2**addr_bits)))
        val *= (2**(data_bits - 1) - 1)
        val = int(val)
        if val < 0:
            val = abs(val)
            val = val ^ ((2**data_bits) - 1)
            val += 1
        f.write("\t\t\t\twhen \"" + to_bin(x,addr_bits) + "\" => \n")
        f.write("\t\t\t\t\tdata <= \"" + to_bin(val, data_bits) + "\";\n")
    f.write("\t\t\t\twhen others => \n")
    f.write("\t\t\t\t\tdata <= \"" + to_bin(0, data_bits) + "\";\n")
    f.write("\t\t\tend case;\n")
    f.write("\t\tend if;\n")
    f.write("\tend process;\n")
    f.write("end Behavioral;\n")
