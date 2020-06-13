module BlackBox(G_i_k, P_i_k, G_kminus1_j, P_kminus1_j, G_i_j, P_i_j);
input G_i_j, P_i_k, G_kminus1_j, P_kminus1_j;
output G_i_j, P_i_j;
assign G_i_j = G_i_k | (P_i_k & G_kminus1_j);
assign P_i_j = P_i_k & P_kminus1_j;
endmodule
