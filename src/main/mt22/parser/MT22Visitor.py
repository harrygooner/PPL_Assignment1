# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arr.
    def visitArr(self, ctx:MT22Parser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayList.
    def visitArrayList(self, ctx:MT22Parser.ArrayListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#non_null_arrayList.
    def visitNon_null_arrayList(self, ctx:MT22Parser.Non_null_arrayListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayEle.
    def visitArrayEle(self, ctx:MT22Parser.ArrayEleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#noninitVardecl.
    def visitNoninitVardecl(self, ctx:MT22Parser.NoninitVardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initVardecl.
    def visitInitVardecl(self, ctx:MT22Parser.InitVardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initVardeclEle.
    def visitInitVardeclEle(self, ctx:MT22Parser.InitVardeclEleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#non_null_exprlist.
    def visitNon_null_exprlist(self, ctx:MT22Parser.Non_null_exprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paradecl.
    def visitParadecl(self, ctx:MT22Parser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#params.
    def visitParams(self, ctx:MT22Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#non_null_params.
    def visitNon_null_params(self, ctx:MT22Parser.Non_null_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#body.
    def visitBody(self, ctx:MT22Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#concat_expr.
    def visitConcat_expr(self, ctx:MT22Parser.Concat_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#concat_operand.
    def visitConcat_operand(self, ctx:MT22Parser.Concat_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_expr.
    def visitRelational_expr(self, ctx:MT22Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_EQ_expr.
    def visitRelational_EQ_expr(self, ctx:MT22Parser.Relational_EQ_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_noEQ_expr.
    def visitRelational_noEQ_expr(self, ctx:MT22Parser.Relational_noEQ_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_EQ_operand.
    def visitRelational_EQ_operand(self, ctx:MT22Parser.Relational_EQ_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_EQ_op.
    def visitRelational_EQ_op(self, ctx:MT22Parser.Relational_EQ_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_noEQ_op.
    def visitRelational_noEQ_op(self, ctx:MT22Parser.Relational_noEQ_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_noEQ_operand.
    def visitRelational_noEQ_operand(self, ctx:MT22Parser.Relational_noEQ_operandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_expr.
    def visitLogical_expr(self, ctx:MT22Parser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_op.
    def visitLogical_op(self, ctx:MT22Parser.Logical_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#add_expr.
    def visitAdd_expr(self, ctx:MT22Parser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mul_expr.
    def visitMul_expr(self, ctx:MT22Parser.Mul_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mul_op.
    def visitMul_op(self, ctx:MT22Parser.Mul_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#nega_expr.
    def visitNega_expr(self, ctx:MT22Parser.Nega_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expr.
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_expr.
    def visitIndex_expr(self, ctx:MT22Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_list.
    def visitIndex_list(self, ctx:MT22Parser.Index_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcall_expr.
    def visitFuncall_expr(self, ctx:MT22Parser.Funcall_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argulist.
    def visitArgulist(self, ctx:MT22Parser.ArgulistContext):
        return self.visitChildren(ctx)



del MT22Parser