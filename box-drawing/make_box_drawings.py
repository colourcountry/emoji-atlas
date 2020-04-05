#!/usr/bin/python

dirs = ["64 0", "128 64", "64 128", "0 64"]

chars = { 
  0x2500: (0,1,0,1),
  0x2501: (0,2,0,2),
  0x2502: (1,0,1,0),
  0x2503: (2,0,2,0),
  0x2504: (0,4,0,4),
  0x2505: (0,5,0,5),
  0x2506: (4,0,4,0),
  0x2507: (5,0,5,0),
  0x2508: (0,6,0,6),
  0x2509: (0,7,0,7),
  0x250a: (6,0,6,0),
  0x250b: (7,0,7,0),
  0x250c: (0,1,1,0),
  0x250d: (0,2,1,0),
  0x250e: (0,1,2,0),
  0x250f: (0,2,2,0),
  0x2510: (0,0,1,1),
  0x2511: (0,0,1,2),
  0x2512: (0,0,2,1),
  0x2513: (0,0,2,2),
  0x2514: (1,1,0,0),
  0x2515: (1,2,0,0),
  0x2516: (2,1,0,0),
  0x2517: (2,2,0,0),
  0x2518: (1,0,0,1),
  0x2519: (1,0,0,2),
  0x251a: (2,0,0,1),
  0x251b: (2,0,0,2),
  0x251c: (1,1,1,0),
  0x251d: (1,2,1,0),
  0x251e: (2,1,1,0),
  0x251f: (1,1,2,0),
  0x2520: (2,1,2,0),
  0x2521: (2,2,1,0),
  0x2522: (1,2,2,0),
  0x2523: (2,2,2,0),
  0x2524: (1,0,1,1),
  0x2525: (1,0,1,2),
  0x2526: (2,0,1,1),
  0x2527: (1,0,2,1),
  0x2528: (2,0,2,1),
  0x2529: (2,0,1,2),
  0x252a: (1,0,2,2),
  0x252b: (2,0,2,2),
  0x252c: (0,1,1,1),
  0x252d: (0,1,1,2),
  0x252e: (0,2,1,1),
  0x252f: (0,2,1,2),
  0x2530: (0,1,2,1),
  0x2531: (0,1,2,2),
  0x2532: (0,2,2,1),
  0x2533: (0,2,2,2),
  0x2534: (1,1,0,1),
  0x2535: (1,1,0,2),
  0x2536: (1,2,0,1),
  0x2537: (1,2,0,2),
  0x2538: (2,1,0,1),
  0x2539: (2,1,0,2),
  0x253a: (2,2,0,1),
  0x253b: (2,2,0,2),
  0x253c: (1,1,1,1),
  0x253d: (1,1,1,2),
  0x253e: (1,2,1,1),
  0x253f: (1,2,1,2),
  0x2540: (2,1,1,1),
  0x2541: (1,1,2,1),
  0x2542: (2,1,2,1),
  0x2543: (2,1,1,2),
  0x2544: (2,2,1,1),
  0x2545: (1,1,2,2),
  0x2546: (1,2,2,1),
  0x2547: (2,2,1,2),
  0x2548: (1,2,2,2),
  0x2549: (2,1,2,2),
  0x254a: (2,2,2,1),
  0x254b: (2,2,2,2),
  0x254c: (0,8,0,8),
  0x254d: (0,9,0,9),
  0x254e: (8,0,8,0),
  0x254f: (9,0,9,0),
  0x2550: (0,3,0,3),
  0x2551: (3,0,3,0),
  0x2552: (0,3,1,0),
  0x2553: (0,1,3,0),
  0x2554: (0,3,3,0),
  0x2555: (0,0,1,3),
  0x2556: (0,0,3,1),
  0x2557: (0,0,3,3),
  0x2558: (1,3,0,0),
  0x2559: (3,1,0,0),
  0x255a: (3,3,0,0),
  0x255b: (1,0,0,3),
  0x255c: (3,0,0,1),
  0x255d: (3,0,0,3),
  0x255e: (1,3,1,0),
  0x255f: (3,1,3,0),
  0x2560: (3,3,3,0),
  0x2561: (1,0,1,3),
  0x2562: (3,0,3,1),
  0x2563: (3,0,3,3),
  0x2564: (0,3,1,3),
  0x2565: (0,1,3,1),
  0x2566: (0,3,3,3),
  0x2567: (1,3,0,3),
  0x2568: (3,1,0,1),
  0x2569: (3,3,0,3),
  0x256a: (1,3,1,3),
  0x256b: (3,1,3,1),
  0x256c: (3,3,3,3),
  0x2574: (0,0,0,1),
  0x2575: (1,0,0,0),
  0x2576: (0,1,0,0),
  0x2577: (0,0,1,0),
  0x2578: (0,0,0,2),
  0x2579: (2,0,0,0),
  0x257a: (0,2,0,0),
  0x257b: (0,0,2,0),
  0x257c: (0,2,0,1),
  0x257d: (1,0,2,0),
  0x257e: (0,1,0,2),
  0x257f: (2,0,1,0)
}

for code,ends in chars.items():
  paths = ['<svg enable-background="new 0 0 128 128" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg">']
  for weight in range(4):
    down = False
    to_draws = [x==weight for x in ends]
    d = ""
    for dir,to_draw in enumerate(to_draws):
      if to_draw:
        if down:
          d += f"L {dirs[dir]} "
          down = False
        else:
          cx = 64
          cy = 64
          nudge = 0
          if weight==1:
            if ends[(dir+1)%4]==0 and ends[(dir-1)%4]>1:
              nudge = ends[(dir-1)%4]*8
            elif ends[(dir-1)%4]==0 and ends[(dir+1)%4]>1:
              nudge = ends[(dir+1)%4]*8
          if dir//2==0:
            nudge=-nudge
          if dir%2==0:
            nudge=-nudge
            cy+=nudge
          else:
            cx+=nudge
          d += f"M {dirs[dir]} L {cx} {cy} "
          down = True
    if d:
      paths.append(f'<path stroke="#eee" fill="none" stroke-width="{weight*16}" d="{d}" />')
      if weight==3:
        paths.append(f'<path stroke="#222" fill="none" stroke-width="16" d="{d}" />')

  paths.append("</svg>")

  with open("svg/"+hex(code)+".svg","w") as f:
    f.writelines(paths)


