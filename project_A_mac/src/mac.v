// simple MAC (Multiply-Accumulate)
module mac (
  input clk,
  input rst,
  input signed [15:0] a,
  input signed [15:0] b,
  output reg signed [31:0] acc
);
  always @(posedge clk or posedge rst) begin
    if (rst) acc <= 0;
    else acc <= acc + a * b;
  end
endmodule
