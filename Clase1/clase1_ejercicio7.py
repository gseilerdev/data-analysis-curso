valor_a = "42"
valor_b = "3.14"
valor_c = "True"
valor_d = ""
valor_e = "N/A"
valor_f = "  150  "
valor_g = "$1,250.50"
valor_h = "01/03/2024" 
valor_a_int = int(valor_a)
valor_b_float = float(valor_b)
valor_c_bool = valor_c == "True"
valor_d_bool = None
valor_e_bool = None
valor_f_int = int(valor_f.strip())
valor_g_float = float(valor_g.replace("$", "").replace(",", ""))
valor_h_date = valor_h