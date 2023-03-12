import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
#     def test_simple_initvardecl(self):
#         """Simple program: int main() {} """
#         input = """a,b,c: string = expr,expr,expr;"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 201))
#     def test_simple_program(self):
#         """Simple program: int main() {} """
#         input = """main:function void(){}"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 202))

#     def test_simple_string_concat(self):
#         """Simple program: int main() {} """
#         input = """{\"Kangxi\", \"Yongzheng\", \"Qianlong\"}
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 333))
    
        
#     def test_simple_pro(self):
#         """Simple program: int main() {} """
#         input = """ fact: function integer (n: integer){
#         if (n == 0) return 1;
#                     else return n*fact(n-1);            
#         }    
#         inc: function void (out n: integer, delta: integer){
#             n = n + delta;
#         }
#         main: function void(){
#             delta: integer = fact(3);
#             inc(x, delta);
#             printInteger(x);
#         }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 207))    
#     def test_simple_prog(self):
#         """Simple program: int main() {} """
#         input = """ for(i = 0, i < 10, i+1){
#         r, s: int;
# r = 2.0;
#             a, b: array [5] of int;
#         s = r * r * myPI;
#         a[0] = s;
#         }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 208))

#     def test_simple_funcstmt(self):
#         """Simple program: int main() {} """
#         input = """foo(2 + x, 4.0 / y);
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 209))

# Variable declarations
    def test1(self):
        """Simple program"""
        input = """main: function void() { }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test2(self):
        """Simple program"""
        input = """main: function auto() { 
            return 1
        }"""
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test3(self):
        """Simple program"""
        input = """main: function void() {
            a : integer;
         }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test4(self):
        """Simple program"""
        input = """main: function void() { 
            a : integer = 4;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test5(self):
        """Simple program """
        input = """main: function void(inherit out a: array [1+1,2] of integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test6(self):
        """Simple program """
        input = """main: function void(out a: array [1+1,2] of void) { }"""
        expect = "Error on line 1 col 44: void"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test7(self):
        """Simple program"""
        input = """main: function void() {
            do{ a = a+1;}
            while (1==2);
         }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test8(self):
        """Simple program"""
        input = """main: function void() { 
            do{ a : auto = fact(a+1);}
            while (1==2);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test9(self):
        """Simple program """
        input = """main: function void() { 
            do{ a : auto = readInteger();}
            while (1==2);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test10(self):
        """Simple program """
        input = """Super(A);"""
        expect = "Error on line 1 col 5: ("
        self.assertTrue(TestParser.test(input, expect, 210))


    def test11(self):
        """Simple program """
        input = """x : integer = 65;
                    fact : function integer ( n : integer) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test12(self):
        """Simple program """
        input = """inc : function void ( out n : integer , d :n = n + delta ;
        }"""
        expect = "Error on line 1 col 43: n"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test13(self):
        """Simple program """
        input = """inc : function void ( out n : integer , d : auto = n + delta ;
        }"""
        expect = "Error on line 1 col 49: ="
        self.assertTrue(TestParser.test(input, expect, 213))

    def test14(self):
        """Simple program"""
        input = """inc : function void ( out n : integer , d : auto){
        
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test15(self):
        """Simple program """
        input = """inc : function void ( out n : integer , d : auto){
                    array: int = 10;
                }"""
        expect = "Error on line 2 col 20: array"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test16(self):
        input = """BFS: function void(inherit node: string) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test17(self):
        input = """Genetic_al: function void(params: string) inherit algorithm {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test18(self):
        input = """how_to_pass_SE: function string(out rate: float) inherit CSE {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test19(self):
        input = """roll_at_level_8: function boolean(champ: string, rate: array [5] of float) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test20(self):
        input = """findtheroad: function array [10] of string(roadmap: string) inherit ggmap {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    # Assignment statements
    def test21(self):
        input = """main: function void() {
                    a = 2;
                    b = "string";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test22(self):
        input = """main: function void() {
                    c = true;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test23(self):
        input = """main: function void() {
                    d[1,2] = {1,2,3};
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test24(self):
        input = """main: function void() {
                    pi = 3.14;
                    S = r * r * pi;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test25(self):
        input = """main: function void() {
                    math = 10;
                    physics = 9.25;
                    chemistry = 8.25;
                    ovr = math + physics + chemistry;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test26(self):
        input = """main: function void() {
                    a = 5 + 2;
                    b[2] = 5 * 4;
                    c = 5 / 3;
                    d[1] = (a + b) * (c / 2);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test27(self):
        input = """main: function void() {
                    a = true;
                    b = false;
                    flag = a && b || (a && b);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test28(self):
        input = """main: function void() {
                    result = cal(a,b,c);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test29(self):
        input = """main: function void() {
                    a = 5 > 2;
                    b = 7 <= 3;
                    c = (1 < 5) >= (5 % 2);
                    d = !(5 < 4);
                    e = !a && b || c && (d && 1);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test30(self):
        input = """main: function void() {
                    str[0] = "111" + "222";
                    str1[1,2] = str::"333";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    # If statements
    def test31(self):
        input = """is_pass: function void(grade: float) {
                    if (grade >= 5.0) print("Is passed");
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test32(self):
        input = """is_pass: function void(grade: float) {
                    if (grade >= 5.0) print("Is passed");
                    else print("You still pass, but pass away");
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test33(self):
        input = """is_pass: function void(grade: float) {
                    if (grade >= 8.0) print("Excellent");
                    else if (grade >= 5.0) print("Is passed");
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test34(self):
        input = """is_pass: function void(grade: float) {
                    if (grade >= 8.0) print("Excellent");
                    else if (grade >= 5.0) print("Is passed");
                    else print("Good luck next time");
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test35(self):
        input = """nenkiembokhong: function string() {
                    if (random(seed) >= 0.5) return "nen";
                    else {
                        print("Random lai di");
                        return "khong";
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test36(self):
        input = """truonganhngoc: function string(cmt: string) {
                    if (cmt == "Tin chuan chua anh?") return "Chuan em nhe!";
                    else return "Anh song nhu the day em";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test37(self):
        input = """NicoloZaniolo: function string(quote: string) {
                    if (dribble) return "Chuyen di dung sut";
                    else if (shoot) return "Anh khong nghe toi";
                    else if (no_goal) return "Anh khong an mung";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test38(self):
        input = """quote_list: function array [3] of string() {
                    if (is_reply) return {"Comment nang ne qua, ban thua do a`"
                            , "Em dien hoi canh sat Los Angeles nhe"
                            , "Khoan da chung ta can phai check VAR"};
                    else return "Ban se bi block";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test39(self):
        input = """roll_or_die: function boolean (flag: boolean) inherit main {
                    if (random > 3) return true;
                    else return false;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test40(self):
        input = """quamonPPL: function auto() {
                    if (1 == 1) return "Rot mon";
                    else print("Cung la rot mon");
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    # For statements
    def test41(self):
        input = """main: function void() {
                    for (i = 1, i < 10, i + 1) {
                        writleInt(i);
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test42(self):
        input = """main: function void() {
                    for (i = 5*8, a < 10+2, b / 2) writleInt(i);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test43(self):
        input = """main: function void() {
                    for (abc = z, i < y, a + func(5)) {}
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test44(self):
        input = """main: function void() {
                    for (y = a && b, a || b, a::c) z = 1;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test45(self):
        input = """main: function void() {
                    for (i = z, i < 5, j >= 1) a = func(1*2);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test46(self):
        input = """main: function void() {
                    for (i = 1, i < 10, i + 1) {
                        writleInt(i);
                    }
                    for (i = 1, i < 10, i + 1) {
                        writleInt(i);
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test47(self):
        input = """main: function void() {
                    for (i = 1, i < 10, i + 1) continue;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test48(self):
        input = """main: function void() {
                    for (i = 1, i < 10, i + 1) {
                        if (i == 5) break;
                        else print(i);
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test49(self):
        input = """main: function void() {
                    for (i = 1, i < 10, i + 2) {
                        i = i + 1;
                        foo(xyz);
                        {
                            a = a + 1;
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test50(self):
        input = """main: function void() {
                    for (i = 1, i < 10, i + 1) {
                        while (i == 1) i = 0;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    # While statements
    def test51(self):
        input = """main: function void() {
                    while (i < 5) {
                        i = i + 1;
                        print("It's 10");
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test52(self):
        input = """main: function void() {
                    while (i < 10) {print(\"Haha\");}
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test53(self):
        input = """main: function void() {
                    while (ity < yza) print(a);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test54(self):
        input = """main: function void() {
                    while (i + 5) a = "str";
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test55(self):
        input = """main: function void() {
                    while (i :: 0.5) {
                        for (t = 0, t < 5, t + 1) {
                            break;
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test56(self):
        input = """main: function void() {
                    while (i < 7) {
                        do {
                            check(count,b,z,t);
                        }
                        while (x + y);
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test57(self):
        input = """main: function void() {
                    while (j == 0) {
                        call(0.5,2,"str",{1,2,3});
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test58(self):
        input = """main: function void() {
                    while (i + i + z) break;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test59(self):
        input = """main: function void() {
                    while (z / 5) {
                        i = i + 1;
                        continue;
                        iyz = ppl(hk222);
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test60(self):
        input = """main: function void() {
                    while (i < 5) if (i == 1) {
                        i = 5; break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    # Do-while statements
    def test61(self):
        input = """main: function void() {
                    do {} while (i + 1);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test62(self):
        input = """main: function void() {
                    do {call(xyz);} while (a * b);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test63(self):
        input = """main: function void() {
                    do 
                    {
                        {
                            a =a+a+a*a;
                        }
                    } 
                    while (i + 1);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test64(self):
        input = """main: function void() {
                    do { tr = true; } while ("str" + false + 1 + 0.5);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test65(self):
        input = """main: function void() {
                    do {_tttt = 1 + 2;} while (expr + expr);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test66(self):
        input = """main: function void() {
                    do {return 1;} while (a && b);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test67(self):
        input = """main: function void() {
                    do {break;} while (foo(abc));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test68(self):
        input = """main: function void() {
                    do {while (t+z) {}} while (2 + a);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test69(self):
        input = """main: function void() {
                    do {call(22,11,33); continue; return 1;} while (aa);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test70(self):
        input = """main: function void() {
                    do {{{{return 1;} return 2;} return 3;} return 4;} while (z);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    # Combine all declarations and statements
    def test71(self):
        input = """main: function void() {
                    pi: float = 3.14;
                    n: float;
                    n = 5.0;
                    S = pi * square(n);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test72(self):
        input = """main: function void() {
                    sum: integer = 0;
                    arr: array[5] of integer;
                    arr = {5,6,7,8,9};
                    for (i = 0, i < 5, i+1) {
                        print(cube(arr[i]));
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test73(self):
        input = """main: function void() {
                    x = x + 1;
                    y = y + 1;
                    z = z + 1;
                    a, b, c: string = "How", "are", "you";
                    if (x == y) {
                        a = b;
                        b = c;
                    }
                    else if (y == z) {
                        b = c;
                        c = a;
                    }
                    else {
                        c = a;
                        a = b;
                    }
                    concat(a, b, c);    
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test74(self):
        input = """
                    f: function integer(out a: string) inherit vod {
                        do {
                            a = a + 1;
                        }
                        while (i + 1);
                        return a;
                    }
                    z: function string( t: auto) {
                        for (j = 0, j < 5, j+1) {
                            if (j == 2) continue;
                            else if (j == 4) return j;
                        }
                        return "abc";
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test75(self):
        input = """a,b,c : integer = 1, 1_2_3, 3, 6;"""
        expect = "Error on line 1 col 29: ,"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test76(self):
        input = """a: integer = 3+4*5;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test77(self):
        input = """fact: function integer (n: integer) {
                    a = 4;
                    if (a>3) a = 5;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test78(self):
        input = """inc: function void (out n: integer, delta: integer) {
                    a = 2;
                    b = 3;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test79(self):
        input = """fact: function integer (n: integer) {
            a = 4;
            if (a>3) {
                a = a + 3;
                b = a && b + 4;
            }
            else a = 7;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test80(self):
        input = """main: function void() {
                    do {return 132213;} while (dsfdw / dfsfdsl + (sdfds - fdbkfds));
                    rewdsjfewp = dfshdfsfds + _dfshdfs_sdfhdfssdf;
                    fdfdhwf(sdfdsf,{123,213,13,aaa,weew});
                    for (i = 0, i > 5, i - 1) {
                        for (i = 0, i > 5, i - 1) {
                            for (i = 0, i > 5, i - 1) {
                                for (i = 0, i > 5, i - 1) {
                                    return;
                                }
                            }
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    # Catch errors
    def test81(self):
        input = """dsfhfdslfds: integer = false;
                    fsdffsdsdf: float = fdsfdsfds;
                    sfw, sdfhsdfo, dsfodsfhw: string = {1,2,3,4}, sdhfowe, "sfsdhow";
                    fhslfdsf: function array [1,1,1,1,1,1,1,1,1] of string (inherit out dshfsdldsffd: float) inherit main {
                        return;
                        return;
                        return;
                        return;
                        dfdsfds = fdslfdsf + dsjkfkds;
                        eqwr = fdshlfw[0,1,fdsfdsfds] + fdslfdldfsjlfd;
                    }
                    fsdhdfsdf, sdfwe, fwewro: integer = 432, 324432;
                    dfsfsd: function string () {
                        sdfdsfds[1,2,2+3,(223+22+dsafr)] = dfshfdsl + fdshlfdsf[0,1,{2.4}];
                        call(dsfhfdsldsf,rewro,"123213");
                    }
                """
        expect = "Error on line 12 col 67: ;"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test82(self):
        input = """x: integer = 65;
                fact: function integer (n: integer) {
                    if (n == 0) return 1;
                    else return n * fact(n - 1);
                }
                inc: function void(out n: integer, delta: integer) {
                    n = n + delta;
                }
                main: function void() {
                    delta: integer = fact(3);
                    inc(x, delta);
                    printInteger(x);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test83(self):
        input = """sdfdsf: integer = 2,3,4;
                reerwrewr: fperewprerw = 324324432;
                ffddsfdssdsdfdsf, fdsfwewrrew: function void() {

                }"""
        expect = "Error on line 1 col 19: ,"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test84(self):
        input = """sdfddsfd, func: function voidd() {
                    return;
                }"""
        expect = "Error on line 1 col 16: function"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test85(self):
        input = """sdffwfwef: function boolean(out dfwew: string, fddsf: boolean) {
                    ewrewewrwerrew;
                    return;
                }"""
        expect = "Error on line 2 col 34: ;"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test86(self):
        input = """abc: function string(inherit out sdd: string) inherit 123 {
                    dsfd = fsdferwer + fsdlhfep / fdsofdsf;
                    for (idwewr; fdsfewpfew; fdspwer) {
                        {
                            ohohohohohohohohoho;
                        }
                    }
                    rewrpwer: string = "32432434", {13232,{2133,21321},{abdfgfgf}};
                }"""
        expect = "Error on line 1 col 54: 123"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test87(self):
        input = """123: function stringstringstring(out out out: string) inherit inherit {
                    return {
                        return {
                            return {
                                return 123ab;
                            }
                        }
                    }
                }"""
        expect = "Error on line 1 col 0: 123"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test88(self):
        input = """aaaa: function string(out a: integer) {
                    do {
                        return;
                    }
                    while i+i;
                    rewte = function(aaaa, fdssdfodfs, dsffww);
                    sdfdwwprew()
                    aaaa: string = "a123213", dfsfde, 123214;
                    return 123abfds;
                }"""
        expect = "Error on line 5 col 26: i"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test89(self):
        input = """fewrewrewrewrewr: function void() {
                    a = ewwerewr * ;
                    return
                    return
                    return
                    sdfdfdww, ewrwerer = 1;
                    fssdfdsf, rewrerewwer: string = 1,2,3,;
                }"""
        expect = "Error on line 2 col 35: ;"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test90(self):
        input = """wrewprsd: function function() {}"""
        expect = "Error on line 1 col 19: function"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test91(self):
        input = """sdfdsfdsf: function string() {
                    a = dfsfwer / 34324 ;
                    wqeqe = 1234ab + fdsfd2 ;
                    fff: function auto(inherit out t: auto) {
                        return;
                        return;
                    }
                    if a == 2 else {};
                }"""
        expect = "Error on line 3 col 32: ab"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test92(self):
        input = """aaa: auto = {123213,213213};
                fdewew, strings: string = {2313,213123}, 123213
                aaaa, aaaaa, bbbb: string = ;
                fdsfsdfsdfds: auto,string = 24234, 32432432;
                """
        expect = "Error on line 3 col 16: aaaa"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test93(self):
        input = """3324, string: auto = 43432234432;
                    32132121312: function autos () () {
                    2432: string = "321321213", 12321m, 12312321_2333;
                    dsfff = f24324432;
                }
                """
        expect = "Error on line 1 col 0: 3324"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test94(self):
        input = """dsrwewre: integer = 213214_213213, dffdsb;
                ewqrew, fiewr: function foo(123213);
                dsffwer: boolean = 324324;
                ewrerwerw: function auto(out inherit asadf: string) {

                }
                """
        expect = "Error on line 1 col 33: ,"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test95(self):
        input = """mainnn: function auto(out inherit aaa,aaaa: main) {
                    return;
                }"""
        expect = "Error on line 1 col 26: inherit"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test96(self):
        input = """rrewrerw: integer = 432432234+234324342342;
                aaaaaa = 32442343 / 23423443 * 234324234 : _1213aaaa
                """
        expect = "Error on line 2 col 23: ="
        self.assertTrue(TestParser.test(input, expect, 296))

    def test97(self):
        input = """abcxyz: function str(fsdffsdfsd: string string) {
                    return;
                    return;
                    break;
                    continue;
                }"""
        expect = "Error on line 1 col 17: str"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test98(self):
        input = """ffwer: function auto(string: string) {
                    do {return 132213;} while (dsfdw / dfsfdsl + (sdfds - fdbkfds));
                    rewdsjfewp = dfshdfsfds + _dfshdfs_sdfhdfssdf;
                    fdfdhwf(sdfdsf,{123,213,13,aaa,weew});
                    for (i = 0, i > 5, i - 1) {
                        for (i = 0, i > 5, i - 1) {
                            for (i = 0, i > 5, i - 1) {
                                for (i = 0, i > 5, i - 1) {
                                    return;
                                }
                            }
                        }
                    }
                }"""
        expect = "Error on line 1 col 21: string"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test99(self):
        input = """rewrweuerw: str = 5;"""
        expect = "Error on line 1 col 12: str"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test100(self):
        input = """QuaMonPPL: function auto()(aaaaa: string) {
                    return "Co cai nit";
                }"""
        expect = "Error on line 1 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 300))
