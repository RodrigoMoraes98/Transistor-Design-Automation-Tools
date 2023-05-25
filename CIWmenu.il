procedure( sizingTool()
			printf("Running Sizing Tool...")
			system("LD_LIBRARY_PATH=/lib /bin/python3 ~/SizingTool.py 65")
			
)
procedure( sweepTool()
			printf("Running Sweep Tool...")
			system("LD_LIBRARY_PATH=/lib /bin/python3 ~/SweepTool.py 65")
			
)


;########################Criar menu no terminal CIW##########################
procedure(CreateCIWMenu()
  let( (item1 item2 item3)
    ;; create a couple of menu items
    item1 = hiCreateMenuItem( ?name 'item1 ?itemText "Transistor Sizing Tool"
              ?callback "sizingTool"
            )
    item2 = hiCreateMenuItem( ?name 'item2 ?itemText "Parameter Sweep Tool"
              ?callback "sweepTool()"
            )

	item3 = hiCreateMenuItem( ?name	'item3 ?itemText "About..."
			 ?callback "aboutFunction()"
			)
    ;; create a menu that includes the menu items and return a list of the
    ;; pulldown menus
    hiCreatePulldownMenu('AmitMenu "GAMA Tools" list(item1 item2 item3))
  )
)

procedure(AmitAddMenu(args)
  unless(boundp('AmitMenu)
    CreateCIWMenu()
  )
  list(AmitMenu)
); procedure

procedure(AmitAddToCIW()
  unless(boundp('AmitMenu)
    CreateCIWMenu()
  )
  hiInsertBannerMenu(hiGetCIWindow() AmitMenu  3 )
)

;; create a userMenuTrigger trigger that automatically adds the menu
deRegUserTriggers("maskLayout" nil 'AmitAddMenu)
; may need to initialise CIW menus before adding
ciwMenuInit()
AmitAddToCIW()
