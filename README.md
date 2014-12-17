# 打包方法

因为Android在安装apk时，不对META-INF文件夹的文件经行签名校验，

所以可以在这个文件夹随添加/修改相关文件作为渠道标识


	python ./package.py xxxxx.apk dev



最后一个参数是想要的渠道名称


# 读取渠道包





	public static String getCustomChannelInfo(Context context){

        if(!TextUtils.isEmpty(mChannel)){
            return mChannel;
        }

        mChannel = "default";

        ApplicationInfo appinfo = context.getApplicationInfo();
        String sourceDir = appinfo.sourceDir;
        Log.d("getChannel sourceDir", sourceDir);

        ZipFile zf = null;
        InputStream in = null;
        ZipInputStream zin = null;

        try {
            zf = new ZipFile(sourceDir);

            in = new BufferedInputStream(new FileInputStream(sourceDir));
            zin = new ZipInputStream(in);

            ZipEntry ze;
            Enumeration<?> entries = zf.entries();

            while (entries.hasMoreElements()) {
                ZipEntry entry = ((ZipEntry) entries.nextElement());
                Log.d("getChannel getName", entry.getName());
                if( entry.getName().equalsIgnoreCase("META-INF/channel_info")){
                    long size = entry.getSize();
                    if (size > 0) {
                        BufferedReader br = new BufferedReader( new InputStreamReader(zf.getInputStream(entry)));
                        String line;
                        while ((line = br.readLine()) != null) {
                            mChannel = line;
                        }

                        br.close();
                    }
                }

            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        finally {
            if(in != null){
                try {
                    in.close();
                }
                catch (Exception e){

                }
            }

            if(zin != null){
                try {
                    zin.closeEntry();
                }
                catch (Exception e){

                }
            }

            if(zf != null){
                try {
                    zin.closeEntry();
                }
                catch (Exception e){

                }
            }
        }

        Log.d("getChannel", mChannel);

        return mChannel;

    }
