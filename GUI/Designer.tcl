#############################################################################
# Generated by PAGE version 4.21
#  in conjunction with Tcl version 8.6
#  Jun 17, 2019 03:42:17 PM +0300  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI} -size 12 -weight bold -slant roman -underline 1 -overstrike 0" \
    user \
    vTcl:font9
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#2b3f77} 
    wm focusmodel $top passive
    wm geometry $top 1200x1000+450+0
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3844 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "VRI - Designer"
    vTcl:DefineAlias "$top" "Designer" vTcl:Toplevel:WidgetProc "" 1
    canvas $top.can43 \
        -background {#45bfe8} -borderwidth 2 -closeenough 1.0 -height 193 \
        -insertbackground black -relief ridge -selectbackground {#c4c4c4} \
        -selectforeground black -width 213 
    vTcl:DefineAlias "$top.can43" "env_canvas" vTcl:WidgetProc "Designer" 1
    entry $top.ent44 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$top.ent44" "file_name" vTcl:WidgetProc "Designer" 1
    button $top.but45 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#45bfe8} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Exit 
    vTcl:DefineAlias "$top.but45" "back" vTcl:WidgetProc "Designer" 1
    bind $top.but45 <Button-1> {
        lambda e: xxx(e)
    }
    label $top.lab46 \
        -background {#2b3f77} -disabledforeground {#a3a3a3} \
        -font {-family {Segoe UI} -size 12 -weight bold -underline 1} \
        -foreground {#ffffff} -text {Environment file name:} 
    vTcl:DefineAlias "$top.lab46" "Label1" vTcl:WidgetProc "Designer" 1
    button $top.but47 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#45bfe8} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text PreView 
    vTcl:DefineAlias "$top.but47" "ve" vTcl:WidgetProc "Designer" 1
    bind $top.but47 <Button-1> {
        lambda e: xxx(e)
    }
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.can43 \
        -in $top -x 0 -y 0 -width 1000 -relwidth 0 -height 1000 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent44 \
        -in $top -x 1020 -y 180 -anchor nw -bordermode ignore 
    place $top.but45 \
        -in $top -x 1020 -y 920 -width 167 -relwidth 0 -height 44 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 1010 -y 140 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 1020 -y 220 -width 167 -relwidth 0 -height 44 \
        -relheight 0 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

