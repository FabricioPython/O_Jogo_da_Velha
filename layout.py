from rich.console import Group, Console
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text


def render_lay(*args):
    a, b, c,d, e, f, g, h, i = args

    grupo = Group(
        
        Columns(
            
        [  
            
            #Título
            Panel(
                Text("# JOGO DA VELHA #",
                      justify='center', 
                      style='b blink bright_white on purple4'), 
                    
            width=23, style="purple4"),

            # A - C
            Columns(

            (   #A1
                Panel(
                    
                    Text(a, justify='center', style="b red"),
                    width=7, 
                    height=3, 
                    subtitle="¹",
                    title_align="center",
                    style="purple4",
                    border_style="b"),
                #B2
                Panel(
                    
                    Text(b, justify='center', style="b red"),
                    width=7, 
                    height=3, 
                    subtitle="²",
                    title_align="center",
                    style="purple4",
                    border_style="b"),
                #C3
                Panel(
                    
                    Text(c, justify='center', style="b red"),
                    width=7,
                    height=3, 
                    subtitle="³",
                    title_align="center",
                    style="purple4",
                    border_style="b")
                )
            ),

            # D - F
            Columns(

            (   #D4
                Panel(
                    
                    Text(d, justify='center', style="b red"),
                    width=7,
                    height=3, 
                    subtitle="⁴",
                    title_align="center",
                    style=" purple4",
                    border_style="b"), 
                #E5
                Panel(
                    
                    Text(e, justify='center', style="b red"),
                    width=7,
                    height=3, 
                    subtitle="⁵",
                    title_align="center",
                    style=" purple4",
                    border_style="b"),
                #F6
                Panel(
                    
                    Text(f, justify='center', style="b red"),
                    width=7,
                    height=3, 
                    subtitle="⁶",
                    title_align="center",
                    style=" purple4",
                    border_style="b")
                )
            ),

            # G - I
            Columns(

            (   #G7
                Panel(
                    
                    Text(g, justify='center', style="b red"),
                    width=7,
                    height=3, 
                    subtitle="⁷",
                    title_align="center",
                    style=" purple4", 
                    border_style="b"),
                #H8
                Panel(
                    
                    Text(h, justify='center', style="b red"),
                    width=7,
                    height=3, 
                    subtitle="⁸", 
                    title_align="center",
                    style=" purple4",
                    border_style="b"), 
                #I9
                Panel(
                    
                    Text(i, justify='center',
                    style="b red")
                    ,width=7,
                    height=3, 
                    subtitle="⁹",
                    title_align="center",
                    style="purple4",
                    border_style="b")
                )
            ),
            #footer
            Panel(
                
                Text("# # # #", justify='center', style='b '),
                width=23,
                style="purple4",
                border_style="b") ], align="center")
)
    
    # exibe
    console = Console()
    
    display = Panel(
                grupo, 
                width=50, 
                height=17,
                style="red"
            )
    
    console.rule("[b][blue]GAM[purple4]#[/purple4]ING[blue/][b/]", style="blue")
    console.print(display, justify="center")
    console.rule(style="b blue")

      
    
    console.print("Click Ctrl to play...",
                  style="b blink2 blue",
                  justify="center")

    #tratar return
    return "ByFabricio"
    
