`timescale 1ns/1ps
module mac_tb;
  reg clk, rst;
  reg signed [15:0] a, b;
  wire signed [31:0] acc;
  mac uut(.clk(clk), .rst(rst), .a(a), .b(b), .acc(acc));

  initial begin
    $dumpfile("mac.vcd");
    $dumpvars(0, mac_tb);
    clk = 0; rst = 1; a = 0; b = 0; #10;
    rst = 0;
    // apply some vectors
    a = 2; b = 3; #10; // acc += 6
    a = 4; b = -1; #10; // acc += -4 -> acc total 2
    a = 100; b = 5; #10; // acc += 500 -> acc 502
    a = -10; b = 2; #10; // ...
    #20;
    $finish;
  end

  always #5 clk = ~clk;
endmodule
