import os

metafile = []

def gen_cfg_rout(dpath, ipath, outpath, cfgpath, scen, basin):
	f = open(dpath, 'r')
	r = f.readlines()
	r[2] = ipath + '/%s/%s.dir' % (basin, basin) + '\n'
	r[11] = ipath + '/%s/%s.xmask' % (basin, basin) + '\n'
	r[14] = ipath + '/%s/%s.frac' % (basin, basin) + '\n' 
	r[16] = ipath + '/%s/%s.stnloc' % (basin, basin) + '\n'
	r[18] = ipath + '/%s/sym/%s/fluxes_' % (basin, scen) + '\n'
	r[21] = outpath + '/%s/%s/%s_' % (scen, basin, basin) + '\n'
	if not os.path.exists(outpath + '/' + scen):
		os.mkdir(outpath + '/' + scen)
	if not os.path.exists(outpath + '/' + scen + '/' + basin):	
		os.mkdir(outpath + '/' + scen + '/' + basin)
	if scen == 'hist':
		r[23] = '1949 01 2009 12\n'
		r[24] = '1949 01 2009 12\n'
 	else:
		r[23] = '2010 01 2099 12\n'
		r[24] = '2010 01 2099 12\n'
	w = ''.join(r)
#	print w
	if not os.path.exists(cfgpath + '/' + scen):
		os.mkdir(cfgpath + '/' + scen)
	cfgwpath = cfgpath + ('/%s/rt_in.%s' % (scen, basin))
	metafile.append('./rout %s\n' % (cfgwpath))
	metafile.append('mv -f *.uh_s %s/%s/uh_s\n' % (ipath, basin))
	with open(cfgwpath, 'w') as outfile:
		outfile.write(w)


#1/16 degree
for fn in os.listdir('/home/chesterlab/Bartos/VIC/input/rout/d16'):
	for s in ['hist', 'ukmo_a1b', 'ukmo_a2', 'ukmo_b1', 'echam_a1b', 'echam_a2', 	'echam_b1']:
		gen_cfg_rout('/home/chesterlab/Bartos/VIC/config/rout/d16/rout_input.default_d16', '/home/chesterlab/Bartos/VIC/input/rout/d16', '/home/chesterlab/Bartos/VIC/output/rout/d16', '/home/chesterlab/Bartos/VIC/config/rout/d16', s, fn)

with open('/home/chesterlab/Bartos/VIC/config/rout/d16/rout_sh_run_d16', 'w') as wfile:
	m = ''.join(metafile)
	wfile.write(m)

metafile = []

#1/8 degree
for fn in os.listdir('/home/chesterlab/Bartos/VIC/input/rout/d8'):
	for s in ['hist', 'ukmo_a1b', 'ukmo_a2', 'ukmo_b1', 'echam_a1b', 'echam_a2', 	'echam_b1']:
		gen_cfg_rout('/home/chesterlab/Bartos/VIC/config/rout/d8/rout_input.default_d8', '/home/chesterlab/Bartos/VIC/input/rout/d8', '/home/chesterlab/Bartos/VIC/output/rout/d8', '/home/chesterlab/Bartos/VIC/config/rout/d8', s, fn)

with open('/home/chesterlab/Bartos/VIC/config/rout/d8/rout_sh_run_d8', 'w') as wfile:
	m = ''.join(metafile)
	wfile.write(m)
