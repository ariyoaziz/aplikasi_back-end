PGDMP  ;    $                }            data_mahasiswa    17.5    17.5                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false                       1262    16391    data_mahasiswa    DATABASE     �   CREATE DATABASE data_mahasiswa WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
    DROP DATABASE data_mahasiswa;
                     postgres    false            �            1259    16392 	   mahasiswa    TABLE     �   CREATE TABLE public.mahasiswa (
    nim character varying(20) NOT NULL,
    nama character varying(100),
    jurusan character varying(50),
    angkatan integer,
    ipk numeric(3,2)
);
    DROP TABLE public.mahasiswa;
       public         heap r       postgres    false                      0    16392 	   mahasiswa 
   TABLE DATA           F   COPY public.mahasiswa (nim, nama, jurusan, angkatan, ipk) FROM stdin;
    public               postgres    false    217   �       �           2606    16396    mahasiswa mahasiswa_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.mahasiswa
    ADD CONSTRAINT mahasiswa_pkey PRIMARY KEY (nim);
 B   ALTER TABLE ONLY public.mahasiswa DROP CONSTRAINT mahasiswa_pkey;
       public                 postgres    false    217               �   x�u�;�0���9EO��3#l��`d	���4AI:������Ͽ]�R9"*�c�'S;d;w�a0�)R��F��*������$�V��dŊhQM[�l��W����\�g[i>�[k.�ߢF��j��HR�\gۍ1;8�|��w���SX6�(��H!�3�E�     