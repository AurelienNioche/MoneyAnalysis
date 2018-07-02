--
-- PostgreSQL database dump
--

-- Dumped from database version 10.3
-- Dumped by pg_dump version 10.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO dasein;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO dasein;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO dasein;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO dasein;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO dasein;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO dasein;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO dasein;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO dasein;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO dasein;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO dasein;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO dasein;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO dasein;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: dashboard_connectedtablet; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.dashboard_connectedtablet (
    id integer NOT NULL,
    device_id text NOT NULL,
    tablet_id integer NOT NULL,
    connected boolean NOT NULL,
    time_last_request timestamp with time zone NOT NULL
);


ALTER TABLE public.dashboard_connectedtablet OWNER TO dasein;

--
-- Name: dashboard_connectedtablet_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.dashboard_connectedtablet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_connectedtablet_id_seq OWNER TO dasein;

--
-- Name: dashboard_connectedtablet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.dashboard_connectedtablet_id_seq OWNED BY public.dashboard_connectedtablet.id;


--
-- Name: dashboard_intparameter; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.dashboard_intparameter (
    id integer NOT NULL,
    name text NOT NULL,
    value integer NOT NULL,
    unit text NOT NULL
);


ALTER TABLE public.dashboard_intparameter OWNER TO dasein;

--
-- Name: dashboard_intparameter_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.dashboard_intparameter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dashboard_intparameter_id_seq OWNER TO dasein;

--
-- Name: dashboard_intparameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.dashboard_intparameter_id_seq OWNED BY public.dashboard_intparameter.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO dasein;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO dasein;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO dasein;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO dasein;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO dasein;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO dasein;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO dasein;

--
-- Name: game_boolparameter; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.game_boolparameter (
    id integer NOT NULL,
    name text,
    value boolean
);


ALTER TABLE public.game_boolparameter OWNER TO dasein;

--
-- Name: game_boolparameter_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.game_boolparameter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_boolparameter_id_seq OWNER TO dasein;

--
-- Name: game_boolparameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.game_boolparameter_id_seq OWNED BY public.game_boolparameter.id;


--
-- Name: game_choice; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.game_choice (
    id integer NOT NULL,
    room_id integer,
    player_id integer,
    t integer,
    user_id integer,
    good_in_hand integer,
    desired_good integer,
    success boolean
);


ALTER TABLE public.game_choice OWNER TO dasein;

--
-- Name: game_choice_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.game_choice_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_choice_id_seq OWNER TO dasein;

--
-- Name: game_choice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.game_choice_id_seq OWNED BY public.game_choice.id;


--
-- Name: game_floatparameter; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.game_floatparameter (
    id integer NOT NULL,
    name text NOT NULL,
    value double precision NOT NULL
);


ALTER TABLE public.game_floatparameter OWNER TO dasein;

--
-- Name: game_floatparameter_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.game_floatparameter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_floatparameter_id_seq OWNER TO dasein;

--
-- Name: game_floatparameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.game_floatparameter_id_seq OWNED BY public.game_floatparameter.id;


--
-- Name: game_intparameter; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.game_intparameter (
    id integer NOT NULL,
    name text NOT NULL,
    value integer NOT NULL
);


ALTER TABLE public.game_intparameter OWNER TO dasein;

--
-- Name: game_intparameter_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.game_intparameter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_intparameter_id_seq OWNER TO dasein;

--
-- Name: game_intparameter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.game_intparameter_id_seq OWNED BY public.game_intparameter.id;


--
-- Name: game_probaexchangetraining; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.game_probaexchangetraining (
    id integer NOT NULL,
    desired_good integer NOT NULL,
    good_in_hand integer NOT NULL,
    p_success double precision NOT NULL
);


ALTER TABLE public.game_probaexchangetraining OWNER TO dasein;

--
-- Name: game_probaexchangetraining_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.game_probaexchangetraining_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_probaexchangetraining_id_seq OWNER TO dasein;

--
-- Name: game_probaexchangetraining_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.game_probaexchangetraining_id_seq OWNED BY public.game_probaexchangetraining.id;


--
-- Name: game_room; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.game_room (
    id integer NOT NULL,
    n_user integer,
    t integer,
    t_max integer,
    tutorial_t integer,
    tutorial_t_max integer,
    trial boolean NOT NULL,
    state text,
    n_type integer,
    types text,
    training_t integer,
    training_t_max integer,
    opened boolean NOT NULL,
    counter integer NOT NULL
);


ALTER TABLE public.game_room OWNER TO dasein;

--
-- Name: game_room_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.game_room_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_room_id_seq OWNER TO dasein;

--
-- Name: game_room_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.game_room_id_seq OWNED BY public.game_room.id;


--
-- Name: game_tutorialchoice; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.game_tutorialchoice (
    id integer NOT NULL,
    room_id integer,
    player_id integer,
    t integer,
    user_id integer,
    good_in_hand integer,
    desired_good integer,
    success boolean
);


ALTER TABLE public.game_tutorialchoice OWNER TO dasein;

--
-- Name: game_tutorialchoice_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.game_tutorialchoice_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_tutorialchoice_id_seq OWNER TO dasein;

--
-- Name: game_tutorialchoice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.game_tutorialchoice_id_seq OWNED BY public.game_tutorialchoice.id;


--
-- Name: game_type; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.game_type (
    id integer NOT NULL,
    room_id integer NOT NULL,
    player_id integer NOT NULL,
    user_id integer,
    production_good integer NOT NULL
);


ALTER TABLE public.game_type OWNER TO dasein;

--
-- Name: game_type_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.game_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_type_id_seq OWNER TO dasein;

--
-- Name: game_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.game_type_id_seq OWNED BY public.game_type.id;


--
-- Name: game_user; Type: TABLE; Schema: public; Owner: dasein
--

CREATE TABLE public.game_user (
    id integer NOT NULL,
    room_id integer,
    device_id text,
    player_id integer,
    pseudo text,
    age integer,
    gender text,
    production_good integer,
    consumption_good integer,
    score integer NOT NULL,
    tutorial_done boolean,
    tutorial_score integer,
    state text,
    training_done boolean,
    training_score integer,
    tablet_id integer
);


ALTER TABLE public.game_user OWNER TO dasein;

--
-- Name: game_user_id_seq; Type: SEQUENCE; Schema: public; Owner: dasein
--

CREATE SEQUENCE public.game_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_user_id_seq OWNER TO dasein;

--
-- Name: game_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dasein
--

ALTER SEQUENCE public.game_user_id_seq OWNED BY public.game_user.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: dashboard_connectedtablet id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.dashboard_connectedtablet ALTER COLUMN id SET DEFAULT nextval('public.dashboard_connectedtablet_id_seq'::regclass);


--
-- Name: dashboard_intparameter id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.dashboard_intparameter ALTER COLUMN id SET DEFAULT nextval('public.dashboard_intparameter_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: game_boolparameter id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_boolparameter ALTER COLUMN id SET DEFAULT nextval('public.game_boolparameter_id_seq'::regclass);


--
-- Name: game_choice id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_choice ALTER COLUMN id SET DEFAULT nextval('public.game_choice_id_seq'::regclass);


--
-- Name: game_floatparameter id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_floatparameter ALTER COLUMN id SET DEFAULT nextval('public.game_floatparameter_id_seq'::regclass);


--
-- Name: game_intparameter id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_intparameter ALTER COLUMN id SET DEFAULT nextval('public.game_intparameter_id_seq'::regclass);


--
-- Name: game_probaexchangetraining id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_probaexchangetraining ALTER COLUMN id SET DEFAULT nextval('public.game_probaexchangetraining_id_seq'::regclass);


--
-- Name: game_room id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_room ALTER COLUMN id SET DEFAULT nextval('public.game_room_id_seq'::regclass);


--
-- Name: game_tutorialchoice id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_tutorialchoice ALTER COLUMN id SET DEFAULT nextval('public.game_tutorialchoice_id_seq'::regclass);


--
-- Name: game_type id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_type ALTER COLUMN id SET DEFAULT nextval('public.game_type_id_seq'::regclass);


--
-- Name: game_user id; Type: DEFAULT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_user ALTER COLUMN id SET DEFAULT nextval('public.game_user_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add int parameter	7	add_intparameter
20	Can change int parameter	7	change_intparameter
21	Can delete int parameter	7	delete_intparameter
22	Can add room	8	add_room
23	Can change room	8	change_room
24	Can delete room	8	delete_room
25	Can add user	9	add_user
26	Can change user	9	change_user
27	Can delete user	9	delete_user
28	Can add tutorial choice	10	add_tutorialchoice
29	Can change tutorial choice	10	change_tutorialchoice
30	Can delete tutorial choice	10	delete_tutorialchoice
31	Can add choice	11	add_choice
32	Can change choice	11	change_choice
33	Can delete choice	11	delete_choice
34	Can add bool parameter	12	add_boolparameter
35	Can change bool parameter	12	change_boolparameter
36	Can delete bool parameter	12	delete_boolparameter
37	Can add receipt	13	add_receipt
38	Can change receipt	13	change_receipt
39	Can delete receipt	13	delete_receipt
40	Can add consumer state	14	add_consumerstate
41	Can change consumer state	14	change_consumerstate
42	Can delete consumer state	14	delete_consumerstate
43	Can add consumer task	15	add_consumertask
44	Can change consumer task	15	change_consumertask
45	Can delete consumer task	15	delete_consumertask
46	Can add int parameter	16	add_intparameter
47	Can change int parameter	16	change_intparameter
48	Can delete int parameter	16	delete_intparameter
49	Can add request time	17	add_requesttime
50	Can change request time	17	change_requesttime
51	Can delete request time	17	delete_requesttime
52	Can add float parameter	18	add_floatparameter
53	Can change float parameter	18	change_floatparameter
54	Can delete float parameter	18	delete_floatparameter
55	Can add connected tablet	19	add_connectedtablet
56	Can change connected tablet	19	change_connectedtablet
57	Can delete connected tablet	19	delete_connectedtablet
58	Can add proba exchange training	20	add_probaexchangetraining
59	Can change proba exchange training	20	change_probaexchangetraining
60	Can delete proba exchange training	20	delete_probaexchangetraining
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$100000$Ehl6D0LKwnyE$vl8lIu3x1IZ5fGYnhoaaK9MbH3Uhc3sooyKETl2wJAY=	2018-06-28 13:41:58.491153+02	t	dasein				t	t	2018-04-18 17:36:55.476836+02
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: dashboard_connectedtablet; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.dashboard_connectedtablet (id, device_id, tablet_id, connected, time_last_request) FROM stdin;
35	a7df091c6fe7c3b9972ff5e799722fea	62	f	2018-06-29 17:44:37.970729+02
68	5f78739091db11228ca0e787bbac71a9	95	f	2018-06-29 17:48:57.008216+02
37	a0783fdcb179747e2cbc2c5eb878bb4e	63	f	2018-06-29 17:45:25.529537+02
45	e0b35d8dadf3e61083ee1ef6c240275a	48	f	2018-06-26 20:49:51.779774+02
52	988f57461cc7f11b62f51efea40497c2	49	f	2018-06-26 20:49:52.848783+02
70	16b9e75cef62de5bf2f21abeeb477b3e	86	f	2018-06-29 17:46:35.899125+02
38	727ecce2b3c3a789c328d6fd7a472b5d	61	f	2018-06-29 17:45:09.406025+02
87	395f476b6ed79fd316594a150ce6e81b	23	f	2018-06-29 17:35:11.627775+02
69	41cc54b5b420acd614370b99eefdbcf3	42	f	2018-06-29 17:38:51.780233+02
30	c345ef2c579b17bc35d463a2333abd70	57	f	2018-06-29 17:40:08.084322+02
101	1c89b44db08161555040e486db81fc6a	93	f	2018-06-29 17:49:19.071475+02
42	450cefcf41b93c66703594b6ffca5360	35	f	2018-06-29 17:37:10.334188+02
62	77c8d726885f0ed0c77fdf55ab54b924	102	f	2018-06-26 20:49:51.7831+02
79	62065aa19039fc3267ef1cc3b6d290c1	91	f	2018-06-29 17:47:29.002068+02
85	2747d19a5ec2a38697bbee0ec6f4d7ee	32	f	2018-06-29 17:36:03.003128+02
93	fe9a907772af68b110dc2ee9adf63868	22	f	2018-06-29 17:34:45.994826+02
60	6a9f1b6f97151ed6ea071c34405092c0	50	f	2018-06-29 17:42:53.978125+02
15	1d3deb4efd759075375f25599f6e263a	10	f	2018-06-29 17:34:28.533234+02
24	73091cd4541bf287c48c412154067792	16	f	2018-06-27 14:39:26.704409+02
49	4a1bc6b505bbc7dc3903823131b9e338	37	f	2018-06-29 17:36:13.614008+02
34	26b3c838bbc2caf94615fe5418337b4d	66	f	2018-06-26 20:49:52.253379+02
59	35ee99f9c035858e79a8084f36c144f5	88	f	2018-06-29 17:46:04.014132+02
61	c4ddb92c4d1dc70e8abb30718f01e127	96	f	2018-06-29 17:46:55.734689+02
76	454365621289a9e7a211e7cc7df084cb	98	f	2018-06-29 17:49:30.629813+02
39	7c98373ccaabf59443f8ab0b35542434	54	f	2018-06-27 14:52:16.009283+02
27	87b51ac59ec9afb161b18cdb0283830c	59	f	2018-06-29 17:42:43.154383+02
55	891e9dca12d57472d7d6e6e8abdf4808	45	f	2018-06-29 17:39:48.366556+02
73	dbd5d8e1761f36975a39fe3bed5d1244	84	f	2018-06-29 17:47:44.01662+02
63	22fc46daff5a752c441f094902a9ce39	94	f	2018-06-29 17:48:24.421174+02
9	74f11944fae55af32f557a045fad6cc8	8	f	2018-06-29 17:32:41.503418+02
33	8a0a2f2514618fce642be055ac2ac2b3	55	f	2018-06-29 17:41:02.073517+02
90	d0bf8a3d91266b3d669562bafa207d25	24	f	2018-06-29 17:35:27.273794+02
65	3e4dfda741e96f4e0f3a9cad913f71cd	83	f	2018-06-29 17:46:19.02423+02
82	1d2e9af7e3c95111154168b9c2eb234e	20	f	2018-06-26 18:00:41.775072+02
94	6552b2f842c42593e2cb598800f31504	33	f	2018-06-29 17:36:45.153644+02
91	0a9125697b290c0e9c730bcbffdb43c4	21	f	2018-06-29 17:33:32.187858+02
98	06c0f0224e58839c2417b51919d5bc32	31	f	2018-06-29 17:38:29.323646+02
29	7503b286f3a8135633d0f26b1ba9192d	65	f	2018-06-29 17:43:23.453741+02
14	dd59883c0e2702665b9795c08d5afdbb	9	f	2018-06-29 17:33:49.34213+02
19	18d526311b7d89313ad4d3f6d1222115	4	f	2018-06-29 17:31:16.024592+02
17	147184823853787075ecfd35752ef767	2	f	2018-06-29 17:32:00.196017+02
99	7f9d8f4aca928ba4dce91f68d68df69b	51	f	2018-06-29 17:43:33.337816+02
23	27d90ecf23a885e96d3df12260f2dc35	15	f	2018-06-26 20:49:52.654255+02
11	63382baa02d0118a7f91a0da3b350cc9	18	f	2018-06-26 20:49:53.304703+02
36	4fcaf81e29e9ee87e9b35955b6a9de51	64	f	2018-06-29 17:44:28.601569+02
83	8f55a49c640a099744d286633c390fcb	11	f	2018-06-26 18:01:21.337294+02
80	595d6b2ca16577285ade68741367cc2a	19	f	2018-06-29 17:32:33.085038+02
20	91e27107b148737f950e902bb2e47727	6	f	2018-06-29 17:34:14.796371+02
28	abd9c5a22c4808ca58a6163a290d34ae	58	f	2018-06-29 17:41:34.120174+02
89	14df1f89b80bc167796d33b7cba4ea2c	30	f	2018-06-29 17:38:11.61955+02
74	4c6120f51cce17fceca54324c6027a4e	87	f	2018-06-25 21:17:47.391991+02
84	8c9b3c464877f76dc9d31cbef1900978	14	f	2018-06-26 18:01:51.431083+02
81	22ce034e36f63f2b8e424990e08c99a0	13	f	2018-06-26 18:00:03.336476+02
88	58aa0d97c523dc4fe70e3fa15014d460	28	f	2018-06-26 18:14:28.171721+02
86	c90a1c228e0a2c3b216cbd00ff934202	25	f	2018-06-26 18:12:52.429618+02
92	2235f89cdcaff7ad75ff966d317284e3	27	f	2018-06-26 18:21:24.137302+02
95	721dc5690ba59d8f41a84df107da5f35	29	f	2018-06-26 18:25:46.307814+02
97	f5ee98426db12ce9db7bde794d2c08b8	26	f	2018-06-26 18:28:10.323567+02
100	6046bd3d2b9bf21bab61285e833880e5	101	f	2018-06-26 18:29:53.590046+02
102	f88b465873f1705e2ef9b2494747567c	97	f	2018-06-26 18:32:07.640752+02
103	4a7a5b704b34844697b39a2d07615f28	81	f	2018-06-26 18:34:42.442301+02
104	6076e775765d7a27e1b67ed88d4fbb10	76	f	2018-06-26 18:35:56.646912+02
105	3f1febc8bb1f21e68ff7ffca1a044d8a	77	f	2018-06-26 18:37:03.365245+02
106	2d69424ff7a196727eb2b0fd531d3939	79	f	2018-06-26 18:38:03.780638+02
107	fd16d98fb3a04fff634c080fc6097924	71	f	2018-06-26 18:39:48.179887+02
47	b1e9a379ec5835111da7276453a2038d	41	f	2018-06-29 17:39:31.591895+02
108	811afeab6383932f806f24a8db321b5a	75	f	2018-06-26 18:41:22.721404+02
109	69a3c037849bc4f54463eef62d8a475f	70	f	2018-06-26 18:42:54.14218+02
110	bac9d8e0daeadb4cc827eafcadabe897	68	f	2018-06-26 18:44:08.507157+02
111	acc8f9557d9494037aecf572723641cf	74	f	2018-06-26 18:46:21.889401+02
112	75ff07e8b8e77ade8325d2445bcd8a5d	78	f	2018-06-26 18:46:46.598547+02
113	e2dd18d64996fde3e09460ff6ff8e08f	82	f	2018-06-26 18:48:01.191235+02
115	02c0a527afa57e2a7bebc6977bb44244	69	f	2018-06-26 18:49:09.073063+02
31	d3f9d0e0ed1c645874c81e941b5a84f6	56	f	2018-06-29 17:41:27.087871+02
116	c937dda800cd190e12021a2e4c7d55be	72	f	2018-06-26 18:50:44.024606+02
117	c84d3338837586bf38e42c7addfbeb47	73	f	2018-06-26 18:51:35.538296+02
75	7dd9f90f616c31f96124576f8a0e4722	89	f	2018-06-29 17:45:55.673447+02
25	6802cf327035f1c895886d23a082c735	5	f	2018-06-29 17:30:36.179784+02
13	e797237e80e10562a2b0257330888055	0	f	2018-06-29 17:31:23.90625+02
71	bf753f339611edcadc53f0ef564c3cca	90	f	2018-06-29 17:47:51.265305+02
43	267f8148b1a9ce429fae82eab648ee05	39	f	2018-06-29 17:37:23.979341+02
41	faa3b0b142856499dfc36a39bf69bf16	53	f	2018-06-29 17:44:14.051515+02
56	c8729cbcfb5cacb309baa833889f00b7	34	f	2018-06-29 17:37:31.969164+02
48	298ff49fc06fdf9cf666ef172ed7fa3f	43	f	2018-06-29 17:39:24.741446+02
22	9191f6e1e5ab4a4257d49c0522f18738	7	f	2018-06-29 17:32:21.460389+02
32	f1426d9326aedd73bfd1a36950a5ca0d	67	f	2018-06-27 12:12:08.835389+02
57	17b7116ede46e2574d2c95c6547ba4bf	44	f	2018-06-29 17:38:41.599209+02
77	9213b27c0a4257d6e9cc20ce694ef68e	52	f	2018-06-29 17:43:49.247175+02
18	f0c5f95d6cdd6b187f95b5fc55244436	17	f	2018-06-26 20:49:52.293867+02
26	40632d094a0d75301104c456ae0558e9	60	f	2018-06-29 17:42:05.102063+02
44	0754a04256327c42245fef15aaaf0002	40	f	2018-06-26 20:49:52.292103+02
53	537f221751e513d3b855363cddba89cd	38	f	2018-06-29 17:35:36.27242+02
16	60c1247b16ef6fe16a03c0948dc80142	12	f	2018-06-26 21:24:39.943743+02
46	326ec36b65bbf30b0402920ba31d08f8	46	f	2018-06-26 20:49:51.688865+02
54	ea94591f5f9582a2afaa809e88ecf7ba	47	f	2018-06-26 20:49:52.426239+02
50	69e91856651bf60ae9c69e238dbb3e38	36	f	2018-06-29 17:36:34.826721+02
21	922396aad56eaf0156b6ea51fe90b97c	3	f	2018-06-29 17:30:48.927244+02
78	bf91b3797169a9df7c13b88e168882c0	92	f	2018-06-29 17:50:14.501277+02
118	864d2a29929fd649549522d88ced0d72	80	f	2018-06-26 20:49:51.815644+02
64	f90ba0b4468f1fc97d74dab2b24eb836	85	f	2018-06-26 20:49:51.837882+02
58	16f8c4135e096489c8b417b82c1c4abe	99	f	2018-06-29 17:47:10.205743+02
66	e3446244bafe2b671b1c6875985420a6	100	f	2018-06-29 17:48:38.447096+02
\.


--
-- Data for Name: dashboard_intparameter; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.dashboard_intparameter (id, name, value, unit) FROM stdin;
2	disconnected_timeout	5	seconds
1	message_count	5858	int
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2018-04-19 17:41:00.460033+02	4	BoolParameter object (4)	3		12	1
2	2018-04-19 17:41:00.470124+02	3	BoolParameter object (3)	3		12	1
3	2018-04-19 17:41:00.477184+02	2	BoolParameter object (2)	3		12	1
4	2018-04-19 17:41:00.483702+02	1	BoolParameter object (1)	3		12	1
5	2018-04-24 14:06:02.862134+02	797	User object (797)	3		9	1
6	2018-04-24 14:06:02.87255+02	796	User object (796)	3		9	1
7	2018-04-24 14:06:02.878929+02	795	User object (795)	3		9	1
8	2018-04-24 14:06:02.885016+02	794	User object (794)	3		9	1
9	2018-05-25 17:56:37.082454+02	3	ConsumerState object (3)	2	[{"changed": {"fields": ["choice"]}}]	14	1
10	2018-06-03 19:37:36.289681+02	352	Room object (352)	2	[{"changed": {"fields": ["n_user", "types"]}}]	8	1
11	2018-06-03 23:04:06.725966+02	353	Room object (353)	2	[{"changed": {"fields": ["n_user", "types"]}}]	8	1
12	2018-06-04 00:51:25.256031+02	354	Room object (354)	2	[{"changed": {"fields": ["n_user", "types"]}}]	8	1
13	2018-06-04 01:23:21.666314+02	356	Room object (356)	2	[{"changed": {"fields": ["n_user", "types"]}}]	8	1
14	2018-06-06 13:09:01.64353+02	1	IntParameter object (1)	2	[{"changed": {"fields": ["value"]}}]	16	1
15	2018-06-07 15:37:02.877383+02	1	IntParameter object (1)	2	[{"changed": {"fields": ["value"]}}]	16	1
16	2018-06-07 17:22:37.841965+02	4	IntParameter object (4)	2	[{"changed": {"fields": ["value"]}}]	16	1
17	2018-06-08 14:18:22.006728+02	5324	User object (5324)	3		9	1
18	2018-06-08 15:08:11.354926+02	4	IntParameter object (4)	2	[{"changed": {"fields": ["value"]}}]	16	1
19	2018-06-08 15:12:46.887287+02	6	IntParameter object (6)	3		16	1
20	2018-06-08 15:12:46.893578+02	5	IntParameter object (5)	3		16	1
21	2018-06-08 15:12:55.987209+02	2	IntParameter object (2)	3		16	1
22	2018-06-08 15:27:50.540599+02	9	IntParameter object (9)	3		16	1
23	2018-06-08 15:27:50.733507+02	8	IntParameter object (8)	3		16	1
24	2018-06-08 15:27:57.472242+02	7	IntParameter object (7)	3		16	1
25	2018-06-08 15:28:05.419075+02	1	IntParameter object (1)	2	[{"changed": {"fields": ["value"]}}]	16	1
26	2018-06-08 15:28:26.023941+02	1	IntParameter object (1)	2	[{"changed": {"fields": ["value"]}}]	16	1
27	2018-06-13 19:48:27.966669+02	6	ConnectedTablet object (6)	3		19	1
28	2018-06-13 19:48:27.975727+02	5	ConnectedTablet object (5)	3		19	1
29	2018-06-13 19:48:27.982845+02	4	ConnectedTablet object (4)	3		19	1
30	2018-06-13 19:48:27.989491+02	3	ConnectedTablet object (3)	3		19	1
31	2018-06-13 19:48:27.996423+02	2	ConnectedTablet object (2)	3		19	1
32	2018-06-13 19:48:28.003123+02	1	ConnectedTablet object (1)	3		19	1
33	2018-06-14 18:28:22.438359+02	11	IntParameter object (11)	3		16	1
34	2018-06-14 18:28:22.448746+02	10	IntParameter object (10)	3		16	1
35	2018-06-14 18:28:22.454725+02	4	IntParameter object (4)	3		16	1
36	2018-06-14 18:28:22.460727+02	3	IntParameter object (3)	3		16	1
37	2018-06-14 18:28:22.46663+02	1	IntParameter object (1)	3		16	1
38	2018-06-21 18:57:05.858412+02	2	IntParameter object (2)	2	[{"changed": {"fields": ["value", "unit"]}}]	7	1
39	2018-06-27 12:01:26.759987+02	6048	User object (6048)	2	[{"changed": {"fields": ["tablet_id"]}}]	9	1
40	2018-06-27 12:17:49.583584+02	6062	User object (6062)	2	[{"changed": {"fields": ["tablet_id"]}}]	9	1
41	2018-06-27 14:00:54.707996+02	1	ProbaExchangeTraining object (1)	1	[{"added": {}}]	20	1
42	2018-06-27 14:01:13.623136+02	2	ProbaExchangeTraining object (2)	1	[{"added": {}}]	20	1
43	2018-06-27 14:02:39.41502+02	3	ProbaExchangeTraining object (3)	1	[{"added": {}}]	20	1
44	2018-06-27 14:02:49.737448+02	2	ProbaExchangeTraining object (2)	3		20	1
45	2018-06-27 14:03:09.39933+02	3	ProbaExchangeTraining object (3)	3		20	1
46	2018-06-27 14:03:43.254942+02	4	ProbaExchangeTraining object (4)	1	[{"added": {}}]	20	1
47	2018-06-27 14:04:02.742343+02	5	ProbaExchangeTraining object (5)	1	[{"added": {}}]	20	1
48	2018-06-27 14:04:30.435052+02	6	ProbaExchangeTraining object (6)	1	[{"added": {}}]	20	1
49	2018-06-27 14:04:43.407983+02	7	ProbaExchangeTraining object (7)	1	[{"added": {}}]	20	1
50	2018-06-27 14:05:12.495538+02	8	ProbaExchangeTraining object (8)	1	[{"added": {}}]	20	1
51	2018-06-27 14:05:28.607258+02	9	ProbaExchangeTraining object (9)	1	[{"added": {}}]	20	1
52	2018-06-27 14:05:40.925842+02	10	ProbaExchangeTraining object (10)	1	[{"added": {}}]	20	1
53	2018-06-27 14:05:55.521817+02	11	ProbaExchangeTraining object (11)	1	[{"added": {}}]	20	1
54	2018-06-27 14:06:04.67962+02	12	ProbaExchangeTraining object (12)	1	[{"added": {}}]	20	1
55	2018-06-27 14:06:29.259216+02	13	ProbaExchangeTraining object (13)	1	[{"added": {}}]	20	1
56	2018-06-27 14:06:39.514124+02	14	ProbaExchangeTraining object (14)	1	[{"added": {}}]	20	1
57	2018-06-27 14:07:46.289792+02	8	ProbaExchangeTraining object (8)	3		20	1
58	2018-06-27 14:07:46.540804+02	7	ProbaExchangeTraining object (7)	3		20	1
59	2018-06-27 14:07:46.5491+02	6	ProbaExchangeTraining object (6)	3		20	1
60	2018-06-27 14:40:16.277936+02	6073	User object (6073)	2	[{"changed": {"fields": ["tablet_id"]}}]	9	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	dashboard	intparameter
8	game	room
9	game	user
10	game	tutorialchoice
11	game	choice
12	game	boolparameter
13	game	receipt
14	game	consumerstate
15	game	consumertask
16	game	intparameter
17	game	requesttime
18	game	floatparameter
19	dashboard	connectedtablet
20	game	probaexchangetraining
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-04-12 15:55:42.173664+02
2	auth	0001_initial	2018-04-12 15:55:42.506875+02
3	admin	0001_initial	2018-04-12 15:55:42.596912+02
4	admin	0002_logentry_remove_auto_add	2018-04-12 15:55:42.617599+02
5	contenttypes	0002_remove_content_type_name	2018-04-12 15:55:42.667804+02
6	auth	0002_alter_permission_name_max_length	2018-04-12 15:55:42.689499+02
7	auth	0003_alter_user_email_max_length	2018-04-12 15:55:42.727931+02
8	auth	0004_alter_user_username_opts	2018-04-12 15:55:42.748187+02
9	auth	0005_alter_user_last_login_null	2018-04-12 15:55:42.784685+02
10	auth	0006_require_contenttypes_0002	2018-04-12 15:55:42.793435+02
11	auth	0007_alter_validators_add_error_messages	2018-04-12 15:55:42.819491+02
12	auth	0008_alter_user_username_max_length	2018-04-12 15:55:42.887646+02
13	auth	0009_alter_user_last_name_max_length	2018-04-12 15:55:42.91499+02
14	dashboard	0001_initial	2018-04-12 15:55:42.998479+02
15	game	0001_initial	2018-04-12 15:55:43.460421+02
16	sessions	0001_initial	2018-04-12 15:55:43.60379+02
17	game	0002_auto_20180413_1244	2018-04-13 12:44:57.148632+02
18	game	0003_remove_choice_final_good	2018-04-13 21:00:55.603365+02
19	game	0002_remove_tutorialchoice_final_good	2018-04-15 02:29:17.352212+02
20	game	0002_choice_lock	2018-04-15 02:32:45.84573+02
21	game	0003_auto_20180415_0301	2018-04-15 03:02:04.337763+02
22	game	0004_remove_choice_locked	2018-04-15 03:30:22.177909+02
23	game	0002_room_n_type	2018-04-18 17:27:25.811892+02
24	game	0003_room_types	2018-04-18 17:27:25.856962+02
25	game	0002_auto_20180418_1736	2018-04-18 17:36:21.983672+02
26	game	0003_auto_20180419_1644	2018-04-19 16:44:29.990668+02
27	game	0004_auto_20180425_1407	2018-04-25 14:07:44.996751+02
28	game	0002_room_training_t	2018-05-17 14:23:10.046819+02
29	game	0002_room_training_t_max	2018-05-18 11:14:15.203708+02
30	game	0002_auto_20180518_1504	2018-05-18 15:04:54.478895+02
31	game	0003_receipt	2018-05-23 15:55:35.031361+02
32	game	0004_consumerstate	2018-05-25 11:36:27.924723+02
33	game	0005_auto_20180525_2015	2018-05-25 20:15:24.3789+02
34	game	0006_room_opened	2018-05-25 20:16:30.476456+02
35	game	0007_consumerstate_treating_t	2018-05-31 15:32:18.036156+02
36	game	0008_room_counter	2018-05-31 20:39:48.255318+02
37	game	0009_auto_20180601_2158	2018-06-01 21:58:51.890278+02
38	game	0010_intparameter_requesttime	2018-06-06 12:14:51.2614+02
39	game	0011_auto_20180607_1405	2018-06-07 14:05:11.496689+02
40	game	0012_intparameter	2018-06-07 14:28:24.984963+02
41	dashboard	0002_connectedtablet	2018-06-13 19:21:26.891749+02
42	dashboard	0002_auto_20180613_1937	2018-06-13 19:37:41.421255+02
43	dashboard	0002_delete_connectedtablet	2018-06-13 19:40:32.151596+02
44	dashboard	0003_connectedtablet	2018-06-13 19:40:42.168746+02
45	game	0013_user_tablet_id	2018-06-26 20:50:12.776413+02
46	game	0014_auto_20180627_1159	2018-06-27 11:59:53.056683+02
47	game	0002_probaexchangetraining	2018-06-27 13:57:11.255141+02
48	game	0003_auto_20180627_1424	2018-06-27 14:24:05.6087+02
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
nwvcl1deqjjvudxsrtijnmtdwl2wrlnv	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-05-02 17:37:07.7438+02
chnf3884814b8f23a6756652ed189c90	YTk5YmJiZDFhOTM2NzMxZGJhODQxYmY2YjA2NDFhZTZiZDQ4ZGJlNTp7fQ==	2018-05-09 15:54:20.992426+02
chnc33bba56ef74cc2baacc6c04a169d	YTk5YmJiZDFhOTM2NzMxZGJhODQxYmY2YjA2NDFhZTZiZDQ4ZGJlNTp7fQ==	2018-05-09 15:56:36.19874+02
chn553277e561508ff6e7417d932a211	YTk5YmJiZDFhOTM2NzMxZGJhODQxYmY2YjA2NDFhZTZiZDQ4ZGJlNTp7fQ==	2018-05-09 15:57:27.689371+02
chn1b3f65a723123013ebbcdb0db3946	YTk5YmJiZDFhOTM2NzMxZGJhODQxYmY2YjA2NDFhZTZiZDQ4ZGJlNTp7fQ==	2018-05-09 15:58:10.536299+02
chn6aed9ff5f03db8bdb5d46ade15d28	YTk5YmJiZDFhOTM2NzMxZGJhODQxYmY2YjA2NDFhZTZiZDQ4ZGJlNTp7fQ==	2018-05-09 16:04:13.12685+02
chne54c68c5e462ad261b17713435bbf	YTk5YmJiZDFhOTM2NzMxZGJhODQxYmY2YjA2NDFhZTZiZDQ4ZGJlNTp7fQ==	2018-05-09 16:06:04.162049+02
chn6383dbc6ca2ba5e1176af3328c15f	YTk5YmJiZDFhOTM2NzMxZGJhODQxYmY2YjA2NDFhZTZiZDQ4ZGJlNTp7fQ==	2018-05-09 16:08:34.137476+02
chnbccc4539f5b26f88cb542623a1733	YTk5YmJiZDFhOTM2NzMxZGJhODQxYmY2YjA2NDFhZTZiZDQ4ZGJlNTp7fQ==	2018-05-09 16:10:22.007877+02
chnfd0c07b1e77a39345047495df40ff	YTk5YmJiZDFhOTM2NzMxZGJhODQxYmY2YjA2NDFhZTZiZDQ4ZGJlNTp7fQ==	2018-05-09 16:11:16.315987+02
chn0d5827e1dcb8cf02e807f8880056e	MWQ0YTE2YTY1MDE2ZDY5MWU0OWUwNzk3YTU1MWZmODJjYmZkMjUyMzp7InJvb20tZ3JvdXAiOiIxMjMifQ==	2018-05-09 16:13:19.123894+02
chn94f754e3b040d428cb9b645b1a8d5	MWQ0YTE2YTY1MDE2ZDY5MWU0OWUwNzk3YTU1MWZmODJjYmZkMjUyMzp7InJvb20tZ3JvdXAiOiIxMjMifQ==	2018-05-09 16:14:16.673478+02
chn9a76a43e1e65cc1450b0c08891ded	MWQ0YTE2YTY1MDE2ZDY5MWU0OWUwNzk3YTU1MWZmODJjYmZkMjUyMzp7InJvb20tZ3JvdXAiOiIxMjMifQ==	2018-05-09 16:39:27.135819+02
chn530b381e867f58a501ec18e2e6ee2	MWQ0YTE2YTY1MDE2ZDY5MWU0OWUwNzk3YTU1MWZmODJjYmZkMjUyMzp7InJvb20tZ3JvdXAiOiIxMjMifQ==	2018-05-09 16:39:54.782855+02
chn5664b5222df0f96607e9ac702da00	MWQ0YTE2YTY1MDE2ZDY5MWU0OWUwNzk3YTU1MWZmODJjYmZkMjUyMzp7InJvb20tZ3JvdXAiOiIxMjMifQ==	2018-05-09 16:40:21.277684+02
chn478db194f56287a111235bbc18033	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:30:50.515256+02
chn5758ecb5fac8b3e848a7918ba6769	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:32:01.53341+02
chnf47f72fbd6e0a1ab495002af8e60f	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:35:36.701914+02
chn0bf05b53fcc87eabb2beacebd9f0f	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:37:11.164643+02
chnd04c120c763488038832c5f17707b	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:48:26.100079+02
chn5d1690787e39b9c233e2736c111b9	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:51:04.954705+02
chn28e120435b2018a62646e36b4e237	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:51:52.696608+02
chn0334742b318d1eb94bd7355f90dff	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:53:11.805043+02
chn9eaa37cb1d528dca5377e372b8019	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:53:40.261672+02
chn7b9fca0d68737da4e5713245370cd	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:56:49.310528+02
chn890f48b69808bfc47f631d0bc55e6	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:57:36.518187+02
chnbe0413cec381831b8e57d08a09105	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 19:57:49.066104+02
chnd8b379ab9ffb697806e63b4e122b0	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:00:38.118659+02
chn3e33c9f6999c884e96df3fed9f1f4	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:03:56.066992+02
chn8e0ab0ce10ea5ba9d5956c87cb717	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:06:20.186143+02
chnb01f69ea83273092568882418e09b	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:13:23.724345+02
chnb2a4144ed1fde57b39f5bf4ae9b23	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:14:53.681532+02
chna7cc10698e7b02d2b6f9a3b18489c	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:16:06.604906+02
chna4f60da2bb615ff945692a97358ba	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:17:32.543278+02
chn04307635324907dea56e841daf38a	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:18:29.09458+02
chn65763266606ad05be47dd223afc86	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:20:14.760125+02
chn812e86fc6940b6adfe4fa66e761dc	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:20:28.628979+02
chn8a09b920ef4ffbf9c7609785e5a1e	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:20:31.038128+02
chnc8689fa643e00d9ef8ef70d497834	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:20:39.391668+02
chneef79c9ca081b4d7aad65f48dbf2f	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:22:43.159749+02
chn309289e8a1c9fd266d1c91c2458ac	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:25:52.239512+02
chn95f8a5d5ba93aae0269a8d8ecda0e	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:27:04.322073+02
chn00f154e6bc4f53e741cbeed4e454e	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:30:46.368766+02
chn2d1f978886fd1af3c697cb98dcac3	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:31:30.392481+02
chna9ea80c78b1e77eb56995560ee337	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:33:15.409396+02
chn33966d1475f6e5bd4285b50b26ed3	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:33:59.231845+02
chn00622667077bd9c51a89681c74c81	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:34:53.795164+02
chn91c547337f3b3bb84e075eb09662e	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:36:00.990173+02
chnddeb2ed5a9572d581bf5275025495	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:39:11.026376+02
chnc64716135216b424108a73ca47b3e	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:39:19.574475+02
chn1430f9a63ab78303ba7304283034e	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:45:33.468874+02
chn5eb896b23464fcc98b34e33f51b33	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:09:22.51325+02
chnebba945d9087c109a6ad84e2fe614	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:46:10.347828+02
chn8e16ae20e105b9cdaaecd5490dbe9	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:46:14.569399+02
chnf14d40bb28a24ef9bc633b62e8b52	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:14:55.413299+02
chn983924920f84d2f7e2f33c78bc715	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:46:46.182529+02
chnc1eec2ed8c99a5dace038274d7acd	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:47:20.200783+02
chn176f1874b8e9bcb62c8815b1e9d4c	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:16:38.386308+02
chn53474de1c6c2518d670c5594934a9	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:53:13.663641+02
chn76b2230d2b62caad33f196f6994ea	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:57:02.95815+02
chn5118a78e3af315386307783a1afde	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:17:24.130354+02
chn03535c369498aa3e65c56df204229	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:57:47.451196+02
chn4bf6b3bf41a716f55bab42b7e649c	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:58:53.574168+02
chn1f9583416b9a722753bf143a07eec	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:19:17.354509+02
chna51945f1c48780abd8b31137e78a5	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:59:00.922066+02
chnab2a0feadb3415bf8ce65c7262d09	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 20:59:09.06185+02
chn1a219cd7bc87378ad4de03459668a	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:20:24.141789+02
chn3eb3645660033d3c4f3461e1a53dc	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:00:11.53955+02
chnfc469299030b9c99dc8889a25dbea	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:01:25.901836+02
chn6ee7c17e251978d03ef4f04aeb41f	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:21:46.074113+02
chnca3d65ea3744158c3871c4e045bbd	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:01:50.740075+02
chn498cc4175c036c224f9fc1303fa6f	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:02:47.641272+02
chn8d98c55f2443dc0e25f35af1cd1a3	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:21:52.839265+02
chn0b886fe468e68a97e0949f9041d33	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:03:36.373251+02
chn973af5f0f2fdb49c9798d90c8dcbd	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:04:19.088929+02
chn4e180b9f689daba944739919e7589	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:22:19.313327+02
chn186af833b5ee96ceaeaf97252bdcc	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:05:58.712977+02
chndd5a31f53f3cff965dd343c3a1ca1	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:06:40.039279+02
chn7b2487a80051b893928992e43749f	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:23:18.31761+02
chn411081a812660ee8cfa80228f3720	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:07:34.531861+02
chn7e32e1acce717b6fc014776a1e877	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:08:21.159508+02
chnfc8b2bfd632ceff788a3f36fbeae3	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:23:30.077293+02
chne4d939ded96bd3ee2be64bbd26996	NjIyMDFhNjcyNmU5NTM1ZDYxOTVjMDgwNmFkOWY1NjM3NjY4Y2FkNDp7InJvb20tZ3JvdXAiOiIxMzAifQ==	2018-05-09 21:27:09.317027+02
chnc27ae7a75b982b62a7ceb529370f2	YWU0MTdkZjhiMTVhZTVjNTQ5MjA4NThkZGFkNmQ0NWQ5ZjgwODNkYjp7InJvb20tZ3JvdXAiOiIxMzEifQ==	2018-05-09 21:27:48.514119+02
chn359de2acf213603f508a2a1d4a59b	MzQ5NWI4NGNhNjkyMzJjY2QwYWY5MWFmN2VhNDQ3YjhlMGE0YzljZjp7InJvb20tZ3JvdXAiOiIxMzMifQ==	2018-05-09 21:28:15.183448+02
chn85db7718ee448694139e9fcaf12ef	MDViOGU3M2JjNTFiNWY4YzQxZDdmMjBlNGVkNDU2NTQ0ZWQ2OGQwYTp7InJvb20tZ3JvdXAiOiIxMzUifQ==	2018-05-09 21:30:35.07979+02
chnf628929cd6f128fd8307c18c0e455	MjBjMWQzYWMyNWI4ODZhNzA5YTgxMTBhNzY5MGE0YzRkMTM2NWRiNTp7InJvb20tZ3JvdXAiOiIxMzgifQ==	2018-05-10 12:27:08.059395+02
chn7fadb49a44bef3fdb5fb35c561544	MjBjMWQzYWMyNWI4ODZhNzA5YTgxMTBhNzY5MGE0YzRkMTM2NWRiNTp7InJvb20tZ3JvdXAiOiIxMzgifQ==	2018-05-10 12:28:08.50343+02
chn98d8041e281ce900f82b1f489fe3d	NmMwOGJkNmExOTYxNTc0MGY2YTgwZTlhMTRiOWFlZTQ3ZGNiMWEwODp7InJvb20tZ3JvdXAiOiIxNDIifQ==	2018-05-10 12:28:15.485054+02
chn4a01e6dd203c2d64d714ec779ab57	NTBkMDc0NDcyNjFiMWY1ZWNlODE4OGQyYWE1ODJiZGMyNDI1ZmIwMDp7InJvb20tZ3JvdXAiOiIxNDYifQ==	2018-05-10 12:29:10.291335+02
hjopomb8fcs6wqdcyb95t5t7rxee3zib	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-05-16 18:46:32.263991+02
zswhzaztvu455kwkcsl3k3wp0l7q2ukt	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-05-31 13:56:50.601692+02
d5xpybu69c9d19t7e1zxh1mbi6dqym4b	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-05-31 14:20:05.125212+02
czrzuhipabzfbokez9rw01kfdxelagr6	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-06-01 11:11:02.484463+02
ox0tm1avkh33om634zpx7gqbercpy91f	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-06-08 17:45:08.933231+02
tbg16dliktdorg2gxx777eyhdhctfhbj	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-06-14 14:28:10.081813+02
sa5qjppqxmvoml9ct2e8cvhegj9agbvt	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-06-22 15:45:50.040254+02
h17oblnb9jodbtpm436mc39mdap74nmi	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-06-28 18:04:17.880186+02
rs2untz317lbbtx0vae38x853rm437ky	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-07-05 17:08:52.023725+02
dx9wlw6f0jcss35zupos5cesnjvo4z8e	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-07-10 17:58:06.855674+02
euv352t2xgfzwq9wv0w5vtjkol3iq2qb	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-07-10 17:58:07.859974+02
zho7oogsftxqv0r31e3vhk31a0i5dctc	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-07-12 12:51:05.584414+02
v5z9ny1ui77ctq67qrgg3dojg93655hz	M2ZkZDM0MjA2YTFmMzQwZjg2MDZhYmU1OTlkMzJhZThmYTAwMmNmMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNTBhY2Y3NWUzNjIyYzIyZTZkNGMyNDQ1NTRlY2ZhZjg5MzljMWY2In0=	2018-07-12 13:41:58.500297+02
\.


--
-- Data for Name: game_boolparameter; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.game_boolparameter (id, name, value) FROM stdin;
8	auto_room	f
6	skip_survey	f
9	skip_training	f
7	skip_tutorial	f
5	trial	f
\.


--
-- Data for Name: game_choice; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.game_choice (id, room_id, player_id, t, user_id, good_in_hand, desired_good, success) FROM stdin;
102621	414	19	10	6106	0	1	f
101721	414	1	10	6088	0	2	t
101671	414	0	10	6087	0	2	t
101723	414	1	12	6088	0	2	t
102622	414	19	11	6106	0	1	t
101731	414	1	20	6088	0	1	t
102281	414	12	20	6099	2	0	t
102282	414	12	21	6099	1	2	t
101791	414	2	30	6089	0	1	t
101691	414	0	30	6087	0	2	t
101692	414	0	31	6087	0	2	t
101741	414	1	30	6088	0	2	t
101800	414	2	39	6089	0	1	f
101793	414	2	32	6089	0	2	t
101792	414	2	31	6089	1	2	t
101810	414	2	49	6089	0	1	t
101700	414	0	39	6087	0	2	t
101801	414	2	40	6089	0	1	t
101850	414	3	39	6090	0	2	f
101751	414	1	40	6088	0	2	t
101703	414	0	42	6087	0	2	t
101710	414	0	49	6087	0	2	t
104175	415	14	14	6137	3	0	t
103959	415	9	48	6132	0	3	t
103462	415	0	1	6123	2	3	f
103464	415	0	3	6123	2	3	f
101722	414	1	11	6088	0	2	t
101724	414	1	13	6088	0	2	t
101773	414	2	12	6089	1	2	t
101674	414	0	13	6087	0	2	t
101775	414	2	14	6089	0	1	t
101732	414	1	21	6088	1	2	t
101733	414	1	22	6088	0	2	t
101683	414	0	22	6087	0	2	t
101783	414	2	22	6089	1	2	t
101684	414	0	23	6087	0	2	t
101785	414	2	24	6089	0	1	t
101794	414	2	33	6089	0	1	t
101693	414	0	32	6087	0	2	t
101694	414	0	33	6087	0	2	t
101745	414	1	34	6088	0	1	t
101752	414	1	41	6088	0	2	t
101802	414	2	41	6089	1	2	t
101753	414	1	42	6088	0	2	t
101704	414	0	43	6087	0	2	t
103466	415	0	5	6123	1	3	t
101734	414	1	23	6088	0	2	t
101725	414	1	14	6088	0	1	f
101726	414	1	15	6088	0	2	t
101696	414	0	35	6087	0	2	t
101727	414	1	16	6088	0	2	t
101776	414	2	15	6089	1	2	t
101735	414	1	24	6088	0	2	t
101736	414	1	25	6088	0	2	t
101787	414	2	26	6089	0	2	t
101786	414	2	25	6089	1	2	t
101695	414	0	34	6087	0	2	f
101795	414	2	34	6089	1	2	t
101797	414	2	36	6089	0	1	t
101746	414	1	35	6088	1	2	t
101705	414	0	44	6087	0	2	t
101754	414	1	43	6088	0	2	t
101755	414	1	44	6088	0	2	f
101805	414	2	44	6089	1	2	t
101756	414	1	45	6088	0	2	t
101677	414	0	16	6087	0	2	f
101728	414	1	17	6088	0	2	t
101678	414	0	17	6087	0	2	t
101779	414	2	18	6089	0	1	t
101763	414	2	2	6089	0	1	f
101762	414	2	1	6089	1	2	t
101663	414	0	2	6087	0	2	t
101764	414	2	3	6089	0	1	f
101664	414	0	3	6087	0	2	t
101815	414	3	4	6090	0	1	t
101729	414	1	18	6088	0	2	t
101665	414	0	4	6087	0	1	f
101765	414	2	4	6089	0	2	t
101666	414	0	5	6087	0	2	t
101667	414	0	6	6087	0	2	t
101816	414	3	5	6090	1	2	t
101717	414	1	6	6088	0	2	t
101768	414	2	7	6089	0	2	t
101767	414	2	6	6089	1	2	t
101718	414	1	7	6088	0	2	t
101769	414	2	8	6089	0	1	t
101668	414	0	7	6087	0	2	t
101719	414	1	8	6088	0	1	t
101720	414	1	9	6088	1	0	t
101730	414	1	19	6088	0	1	f
101679	414	0	18	6087	0	2	t
101670	414	0	9	6087	0	2	t
101780	414	2	19	6089	1	2	t
101687	414	0	26	6087	0	2	t
101788	414	2	27	6089	0	1	t
101737	414	1	26	6088	0	2	t
101688	414	0	27	6087	0	2	t
101689	414	0	28	6087	0	2	t
101747	414	1	36	6088	0	2	t
101690	414	0	29	6087	0	2	t
101739	414	1	28	6088	0	2	t
101799	414	2	38	6089	0	2	t
101748	414	1	37	6088	0	2	t
101798	414	2	37	6089	1	2	t
101706	414	0	45	6087	0	2	t
101699	414	0	38	6087	0	2	t
101807	414	2	46	6089	0	1	t
101757	414	1	46	6088	0	2	t
101758	414	1	47	6088	0	2	t
101809	414	2	48	6089	0	2	t
101808	414	2	47	6089	1	2	t
101709	414	0	48	6087	0	2	t
101931	414	5	20	6092	0	1	t
101982	414	6	21	6093	0	2	t
101881	414	4	20	6091	0	2	t
101882	414	4	21	6091	0	2	t
101934	414	5	23	6092	0	1	t
101841	414	3	30	6090	0	2	t
101991	414	6	30	6093	0	2	f
101901	414	4	40	6091	0	2	t
101992	414	6	31	6093	0	2	t
101952	414	5	41	6092	0	1	f
101951	414	5	40	6092	1	2	t
101953	414	5	42	6092	0	1	t
101852	414	3	41	6090	0	2	t
101902	414	4	41	6091	0	2	f
101910	414	4	49	6091	0	2	t
101860	414	3	49	6090	0	2	t
101960	414	5	49	6092	1	2	t
104342	415	17	31	6140	2	0	t
104676	415	24	15	6147	2	0	f
103468	415	0	7	6123	0	2	t
101821	414	3	10	6090	0	1	f
101932	414	5	21	6092	1	2	t
102271	414	12	10	6099	2	0	t
101833	414	3	22	6090	0	2	t
101823	414	3	12	6090	0	2	t
101822	414	3	11	6090	0	2	t
101883	414	4	22	6091	0	2	f
101742	414	1	31	6088	0	2	t
101835	414	3	24	6090	0	2	t
101834	414	3	23	6090	0	2	t
101892	414	4	31	6091	0	2	t
101943	414	5	32	6092	1	2	t
101944	414	5	33	6092	0	1	t
101895	414	4	34	6091	0	2	t
101894	414	4	33	6091	0	2	t
101844	414	3	33	6090	0	2	t
101853	414	3	42	6090	0	2	t
101904	414	4	43	6091	0	1	f
101854	414	3	43	6090	0	2	t
101906	414	4	45	6091	0	1	t
101905	414	4	44	6091	0	1	f
103470	415	0	9	6123	2	3	t
101972	414	6	11	6093	0	2	t
101672	414	0	11	6087	0	2	t
101873	414	4	12	6091	0	2	t
101923	414	5	12	6092	1	2	t
101924	414	5	13	6092	0	1	f
101885	414	4	24	6091	0	2	t
101935	414	5	24	6092	1	2	t
101886	414	4	25	6091	0	2	t
101836	414	3	25	6090	0	2	t
101837	414	3	26	6090	0	2	t
101946	414	5	35	6092	0	1	t
101945	414	5	34	6092	1	2	t
101847	414	3	36	6090	0	2	t
101846	414	3	35	6090	0	2	t
101896	414	4	35	6091	0	2	f
101855	414	3	44	6090	0	2	f
101907	414	4	46	6091	1	0	t
101856	414	3	45	6090	0	2	t
101956	414	5	45	6092	1	2	t
101908	414	4	47	6091	0	1	t
101925	414	5	14	6092	0	1	t
101824	414	3	13	6090	0	2	t
101874	414	4	13	6091	0	2	t
101826	414	3	15	6090	0	2	t
101825	414	3	14	6090	0	2	t
101887	414	4	26	6091	0	2	t
101875	414	4	14	6091	0	2	t
101912	414	5	1	6092	1	2	t
101913	414	5	2	6092	0	1	f
101914	414	5	3	6092	0	1	t
101863	414	4	2	6091	0	2	t
101965	414	6	4	6093	0	2	t
101967	414	6	6	6093	0	2	t
101865	414	4	4	6091	0	2	t
101966	414	6	5	6093	0	2	t
101926	414	5	15	6092	1	2	t
101866	414	4	5	6091	0	2	t
101867	414	4	6	6091	0	2	t
101927	414	5	16	6092	0	1	t
101818	414	3	7	6090	0	1	f
101819	414	3	8	6090	0	2	t
101968	414	6	7	6093	0	2	t
101969	414	6	8	6093	0	2	t
101919	414	5	8	6092	1	2	t
101970	414	6	9	6093	0	2	t
101877	414	4	16	6091	0	2	t
101820	414	3	9	6090	0	2	t
101889	414	4	28	6091	0	2	t
101827	414	3	16	6090	0	2	f
101878	414	4	17	6091	0	2	t
101928	414	5	17	6092	1	2	t
101929	414	5	18	6092	0	1	t
101888	414	4	27	6091	0	2	t
101829	414	3	18	6090	0	2	t
101930	414	5	19	6092	1	2	t
101838	414	3	27	6090	0	2	t
101947	414	5	36	6092	1	2	t
101839	414	3	28	6090	0	2	f
101948	414	5	37	6092	0	1	t
101940	414	5	29	6092	0	1	t
101840	414	3	29	6090	0	2	t
101898	414	4	37	6091	0	2	t
101899	414	4	38	6091	0	1	t
101900	414	4	39	6091	1	0	t
101949	414	5	38	6092	1	2	t
101857	414	3	46	6090	0	2	t
101950	414	5	39	6092	0	1	t
101909	414	4	48	6091	1	0	t
101858	414	3	47	6090	0	2	t
101859	414	3	48	6090	0	2	f
102081	414	8	20	6095	0	1	t
102031	414	7	20	6094	0	1	t
101981	414	6	20	6093	0	2	t
102050	414	7	39	6094	0	1	f
102091	414	8	30	6095	0	1	t
102060	414	7	49	6094	0	2	t
102041	414	7	30	6094	0	2	t
102042	414	7	31	6094	0	2	t
102093	414	8	32	6095	0	1	f
102000	414	6	39	6093	0	2	t
102010	414	6	49	6093	0	2	t
101851	414	3	40	6090	0	2	t
102001	414	6	40	6093	0	2	t
102051	414	7	40	6094	0	2	t
103476	415	0	15	6123	1	3	f
107442	417	9	31	6202	0	3	t
103478	415	0	17	6123	2	3	t
103493	415	0	32	6123	2	3	t
103474	415	0	13	6123	2	3	f
102032	414	7	21	6094	1	2	t
102121	414	9	10	6096	1	0	t
102122	414	9	11	6096	1	0	t
101971	414	6	10	6093	0	2	t
102371	414	14	10	6101	2	0	t
102123	414	9	12	6096	1	0	t
102092	414	8	31	6095	1	2	t
102082	414	8	21	6095	1	2	t
102083	414	8	22	6095	0	1	t
102033	414	7	22	6094	0	2	t
102034	414	7	23	6094	0	2	t
102085	414	8	24	6095	0	1	t
102084	414	8	23	6095	1	2	t
102094	414	8	33	6095	0	1	f
101993	414	6	32	6093	0	2	t
101994	414	6	33	6093	0	2	t
102002	414	6	41	6093	0	2	t
102053	414	7	42	6094	0	2	t
102055	414	7	44	6094	0	2	t
102003	414	6	42	6093	0	2	t
102103	414	8	42	6095	1	2	t
102054	414	7	43	6094	0	2	t
102075	414	8	14	6095	0	1	f
101973	414	6	12	6093	0	2	t
101974	414	6	13	6093	0	2	t
102035	414	7	24	6094	0	2	t
102036	414	7	25	6094	0	2	t
101985	414	6	24	6093	0	2	t
102087	414	8	26	6095	0	1	t
102086	414	8	25	6095	1	2	t
102095	414	8	34	6095	0	1	t
102038	414	7	27	6094	0	2	f
102045	414	7	34	6094	0	2	t
101995	414	6	34	6093	0	2	t
102046	414	7	35	6094	0	2	t
102096	414	8	35	6095	1	2	t
102047	414	7	36	6094	0	1	f
102004	414	6	43	6093	0	2	t
102005	414	6	44	6093	0	2	f
102007	414	6	46	6093	0	2	t
102105	414	8	44	6095	1	2	t
102006	414	6	45	6093	0	2	t
102124	414	9	13	6096	1	2	t
102025	414	7	14	6094	0	2	t
102076	414	8	15	6095	0	1	f
101975	414	6	14	6093	0	2	t
102127	414	9	16	6096	1	0	t
102037	414	7	26	6094	0	2	t
102089	414	8	28	6095	0	1	t
102088	414	8	27	6095	1	2	t
102026	414	7	15	6094	0	2	t
101976	414	6	15	6093	0	2	t
102040	414	7	29	6094	0	2	t
102062	414	8	1	6095	1	2	t
102013	414	7	2	6094	0	1	t
102115	414	9	4	6096	1	0	t
102063	414	8	2	6095	0	1	f
102014	414	7	3	6094	1	2	t
102015	414	7	4	6094	0	2	t
102116	414	9	5	6096	1	0	t
102117	414	9	6	6096	1	0	t
102016	414	7	5	6094	0	2	t
102017	414	7	6	6094	0	2	t
102118	414	9	7	6096	1	0	t
102077	414	8	16	6095	0	1	t
102018	414	7	7	6094	0	2	t
102119	414	9	8	6096	1	0	t
102019	414	7	8	6094	0	2	t
102120	414	9	9	6096	1	0	t
102020	414	7	9	6094	0	1	t
102128	414	9	17	6096	1	0	t
101977	414	6	16	6093	0	2	t
102029	414	7	18	6094	0	1	t
101978	414	6	17	6093	0	2	t
102078	414	8	17	6095	1	2	t
102079	414	8	18	6095	0	1	t
101980	414	6	19	6093	0	2	t
101979	414	6	18	6093	0	2	t
102039	414	7	28	6094	0	2	t
102080	414	8	19	6095	1	2	t
101989	414	6	28	6093	0	2	t
102098	414	8	37	6095	0	1	t
102097	414	8	36	6095	0	1	f
102090	414	8	29	6095	1	2	t
102048	414	7	37	6094	0	1	f
102049	414	7	38	6094	0	2	t
102056	414	7	45	6094	0	2	f
101999	414	6	38	6093	0	2	t
102009	414	6	48	6093	0	2	t
102057	414	7	46	6094	0	2	t
102008	414	6	47	6093	0	2	t
102058	414	7	47	6094	0	2	t
102059	414	7	48	6094	0	2	t
102241	414	11	30	6098	1	0	t
102192	414	10	31	6097	1	0	t
102141	414	9	30	6096	1	0	t
101941	414	5	30	6092	1	2	t
102193	414	10	32	6097	1	0	t
102201	414	10	40	6097	1	0	t
102202	414	10	41	6097	1	0	t
102151	414	9	40	6096	1	0	t
102203	414	10	42	6097	1	0	t
102152	414	9	41	6096	1	0	t
102260	414	11	49	6098	1	0	t
102160	414	9	49	6096	1	0	t
102210	414	10	49	6097	2	0	t
103892	415	8	31	6131	0	3	t
103759	415	5	48	6128	0	3	f
102171	414	10	10	6097	1	0	t
102221	414	11	10	6098	2	0	t
102172	414	10	11	6097	1	0	t
102173	414	10	12	6097	1	0	t
102142	414	9	31	6096	1	0	t
102181	414	10	20	6097	1	0	t
102131	414	9	20	6096	1	0	t
102232	414	11	21	6098	1	0	t
102231	414	11	20	6098	2	0	t
102182	414	10	21	6097	1	0	t
102194	414	10	33	6097	1	0	t
102143	414	9	32	6096	1	0	t
102195	414	10	34	6097	1	0	t
102252	414	11	41	6098	1	2	t
102144	414	9	33	6096	1	0	t
102153	414	9	42	6096	1	0	t
102154	414	9	43	6096	1	0	t
102155	414	9	44	6096	1	0	t
102204	414	10	43	6097	1	0	t
103481	415	0	20	6123	2	3	t
103483	415	0	22	6123	1	2	t
102222	414	11	11	6098	1	2	t
102223	414	11	12	6098	2	0	t
102224	414	11	13	6098	1	0	t
102174	414	10	13	6097	1	0	t
102132	414	9	21	6096	1	0	f
102183	414	10	22	6097	1	0	t
102133	414	9	22	6096	1	0	t
102134	414	9	23	6096	1	0	t
102283	414	12	22	6099	2	0	t
102145	414	9	34	6096	1	0	t
102146	414	9	35	6096	1	0	t
102147	414	9	36	6096	1	0	t
102246	414	11	35	6098	1	0	t
102196	414	10	35	6097	1	0	f
102198	414	10	37	6097	1	0	t
102156	414	9	45	6096	1	0	t
102205	414	10	44	6097	1	0	t
102157	414	9	46	6096	1	0	t
102206	414	10	45	6097	1	0	t
102256	414	11	45	6098	1	2	t
102175	414	10	14	6097	1	0	t
102275	414	12	14	6099	2	0	t
102176	414	10	15	6097	1	0	t
102225	414	11	14	6098	1	2	t
102227	414	11	16	6098	1	0	t
102276	414	12	15	6099	1	2	t
102184	414	10	23	6097	1	0	t
102185	414	10	24	6097	1	0	t
102284	414	12	23	6099	1	2	t
102235	414	11	24	6098	1	0	t
102136	414	9	25	6096	1	0	t
102135	414	9	24	6096	1	0	t
102247	414	11	36	6098	1	0	t
102162	414	10	1	6097	1	0	t
102163	414	10	2	6097	1	0	t
102177	414	10	16	6097	1	0	t
102164	414	10	3	6097	1	0	t
102263	414	12	2	6099	2	0	f
102165	414	10	4	6097	1	0	t
102215	414	11	4	6098	2	0	t
102166	414	10	5	6097	1	0	t
102167	414	10	6	6097	1	0	t
102216	414	11	5	6098	1	2	t
102267	414	12	6	6099	2	0	t
102168	414	10	7	6097	1	0	t
102178	414	10	17	6097	1	0	t
102268	414	12	7	6099	1	2	t
102219	414	11	8	6098	1	0	t
102170	414	10	9	6097	1	0	t
102169	414	10	8	6097	1	0	t
102137	414	9	26	6096	1	0	t
102220	414	11	9	6098	1	2	t
102228	414	11	17	6098	1	2	t
102129	414	9	18	6096	1	0	t
102130	414	9	19	6096	1	0	t
102179	414	10	18	6097	1	0	t
102186	414	10	25	6097	1	0	t
102180	414	10	19	6097	1	0	t
102236	414	11	25	6098	1	2	t
102187	414	10	26	6097	1	0	t
102238	414	11	27	6098	1	0	t
102239	414	11	28	6098	1	0	t
102188	414	10	27	6097	1	0	t
102189	414	10	28	6097	1	0	t
102140	414	9	29	6096	1	0	t
102148	414	9	37	6096	1	0	t
102149	414	9	38	6096	1	0	t
102240	414	11	29	6098	1	0	t
102150	414	9	39	6096	1	0	t
102199	414	10	38	6097	1	0	t
102200	414	10	39	6097	1	0	t
102207	414	10	46	6097	1	0	t
102258	414	11	47	6098	1	0	t
102259	414	11	48	6098	1	0	t
102158	414	9	47	6096	1	0	t
102159	414	9	48	6096	1	0	t
102341	414	13	30	6100	1	0	t
102400	414	14	39	6101	2	0	t
102291	414	12	30	6099	1	0	f
102351	414	13	40	6100	2	0	t
102360	414	13	49	6100	1	0	t
102352	414	13	41	6100	1	0	t
102301	414	12	40	6099	1	2	t
102401	414	14	40	6101	1	2	t
102310	414	12	49	6099	2	0	t
104992	415	30	31	6153	1	2	t
104092	415	12	31	6135	1	2	t
103485	415	0	24	6123	0	1	t
103487	415	0	26	6123	2	3	t
102421	414	15	10	6102	1	0	t
102321	414	13	10	6100	1	0	t
102322	414	13	11	6100	1	0	t
102422	414	15	11	6102	1	0	t
102431	414	15	20	6102	1	0	t
102331	414	13	20	6100	1	0	t
102353	414	13	42	6100	1	0	t
101831	414	3	20	6090	0	2	t
102332	414	13	21	6100	1	0	t
102591	414	18	30	6105	2	1	f
101942	414	5	31	6092	0	1	t
102342	414	13	31	6100	1	0	t
102343	414	13	32	6100	1	0	t
102392	414	14	31	6101	2	0	t
102344	414	13	33	6100	1	0	t
102302	414	12	41	6099	2	0	t
102354	414	13	43	6100	1	0	t
102403	414	14	42	6101	1	2	t
102355	414	13	44	6100	1	0	t
103489	415	0	28	6123	2	3	t
102323	414	13	12	6100	1	0	t
102324	414	13	13	6100	1	0	t
102423	414	15	12	6102	1	0	t
102424	414	15	13	6102	1	0	t
102432	414	15	21	6102	1	0	t
102383	414	14	22	6101	1	2	t
102434	414	15	23	6102	1	0	t
102333	414	13	22	6100	1	2	t
102334	414	13	23	6100	2	0	t
102335	414	13	24	6100	1	0	t
102394	414	14	33	6101	2	0	t
102395	414	14	34	6101	1	0	t
102294	414	12	33	6099	1	2	t
102346	414	13	35	6100	1	0	t
102345	414	13	34	6100	1	0	t
102404	414	14	43	6101	2	0	f
102405	414	14	44	6101	2	0	t
102406	414	14	45	6101	1	0	t
102305	414	12	44	6099	1	2	t
102325	414	13	14	6100	1	0	t
102326	414	13	15	6100	1	0	t
102425	414	15	14	6102	1	0	t
102375	414	14	14	6101	2	0	t
102426	414	15	15	6102	1	0	t
102435	414	15	24	6102	1	0	t
102386	414	14	25	6101	1	0	t
102337	414	13	26	6100	1	0	t
102336	414	13	25	6100	1	0	t
102436	414	15	25	6102	1	0	t
102396	414	14	35	6101	1	0	f
102296	414	12	35	6099	1	2	t
102397	414	14	36	6101	1	2	t
102347	414	13	36	6100	1	2	t
102398	414	14	37	6101	2	0	t
102356	414	13	45	6100	1	0	t
102427	414	15	16	6102	1	0	t
102312	414	13	1	6100	1	0	t
102413	414	15	2	6102	1	0	t
102327	414	13	16	6100	1	0	t
102414	414	15	3	6102	1	0	t
102313	414	13	2	6100	1	0	t
102428	414	15	17	6102	1	0	t
102415	414	15	4	6102	1	0	t
102315	414	13	4	6100	1	0	t
102316	414	13	5	6100	1	0	t
102416	414	15	5	6102	1	0	t
102317	414	13	6	6100	1	0	t
102417	414	15	6	6102	1	0	t
102418	414	15	7	6102	1	0	t
102318	414	13	7	6100	1	0	t
102319	414	13	8	6100	1	0	t
102369	414	14	8	6101	1	0	t
102320	414	13	9	6100	1	0	t
102328	414	13	17	6100	1	2	t
102370	414	14	9	6101	1	2	t
102379	414	14	18	6101	1	0	t
102429	414	15	18	6102	1	0	t
102430	414	15	19	6102	1	0	t
102338	414	13	27	6100	1	0	t
102387	414	14	26	6101	1	2	t
102330	414	13	19	6100	2	0	t
102348	414	13	37	6100	2	0	t
102438	414	15	27	6102	1	0	t
102388	414	14	27	6101	2	0	t
102339	414	13	28	6100	1	0	t
102439	414	15	28	6102	1	0	t
102389	414	14	28	6101	1	2	t
102440	414	15	29	6102	1	0	t
102290	414	12	29	6099	1	0	t
102340	414	13	29	6100	1	0	t
102399	414	14	38	6101	1	2	t
102300	414	12	39	6099	1	0	t
102349	414	13	38	6100	1	2	t
102357	414	13	46	6100	1	0	t
102307	414	12	46	6099	1	2	t
102358	414	13	47	6100	1	0	t
102308	414	12	47	6099	2	0	t
102359	414	13	48	6100	1	0	t
102309	414	12	48	6099	1	2	t
102550	414	17	39	6104	1	2	t
102560	414	17	49	6104	1	0	t
102451	414	15	40	6102	1	0	t
102551	414	17	40	6104	2	0	t
102552	414	17	41	6104	1	0	t
102453	414	15	42	6102	1	0	t
102460	414	15	49	6102	1	0	t
103492	415	0	31	6123	0	2	t
103494	415	0	33	6123	0	2	t
104209	415	14	48	6137	1	2	t
107669	417	14	8	6207	1	0	t
103496	415	0	35	6123	0	2	t
102481	414	16	20	6103	1	0	t
102532	414	17	21	6104	1	0	t
101871	414	4	10	6091	0	2	t
102531	414	17	20	6104	2	0	t
102482	414	16	21	6103	1	2	t
102483	414	16	22	6103	2	0	t
102534	414	17	23	6104	2	0	t
102533	414	17	22	6104	1	2	t
102583	414	18	22	6105	2	1	f
102452	414	15	41	6102	1	0	t
102441	414	15	30	6102	1	0	t
102442	414	15	31	6102	1	0	t
102541	414	17	30	6104	1	2	t
102542	414	17	31	6104	2	0	t
102503	414	16	42	6103	2	0	t
102454	414	15	43	6102	1	0	t
102553	414	17	42	6104	1	2	t
101772	414	2	11	6089	0	1	t
102372	414	14	11	6101	1	0	t
102523	414	17	12	6104	1	0	t
101872	414	4	11	6091	0	2	t
102474	414	16	13	6103	2	0	t
102473	414	16	12	6103	1	2	t
102485	414	16	24	6103	2	0	t
102484	414	16	23	6103	1	2	t
102585	414	18	24	6105	2	1	t
102486	414	16	25	6103	1	2	t
102492	414	16	31	6103	1	2	t
102543	414	17	32	6104	1	0	t
102443	414	15	32	6102	1	0	t
102493	414	16	32	6103	2	1	t
102444	414	15	33	6102	1	0	t
102504	414	16	43	6103	1	2	t
102455	414	15	44	6102	1	0	t
102555	414	17	44	6104	2	0	t
102556	414	17	45	6104	1	0	t
102456	414	15	45	6102	1	0	t
102525	414	17	14	6104	2	0	t
102524	414	17	13	6104	1	2	t
102586	414	18	25	6105	2	1	t
102526	414	17	15	6104	1	0	t
102575	414	18	14	6105	2	0	f
102537	414	17	26	6104	1	0	t
102487	414	16	26	6103	2	1	t
102488	414	16	27	6103	1	2	t
102587	414	18	26	6105	2	1	f
102489	414	16	28	6103	2	0	t
102538	414	17	27	6104	1	2	t
102494	414	16	33	6103	1	2	t
102445	414	15	34	6102	1	0	t
102544	414	17	33	6104	1	2	t
102545	414	17	34	6104	2	0	t
102495	414	16	34	6103	2	0	t
102457	414	15	46	6102	1	0	t
102507	414	16	46	6103	2	0	t
102508	414	16	47	6103	1	0	t
102475	414	16	14	6103	1	2	t
102512	414	17	1	6104	2	0	f
102513	414	17	2	6104	2	0	f
102514	414	17	3	6104	2	0	t
102563	414	18	2	6105	2	1	t
102465	414	16	4	6103	2	0	t
102576	414	18	15	6105	2	1	t
102565	414	18	4	6105	2	1	t
102477	414	16	16	6103	2	0	t
102466	414	16	5	6103	1	2	t
102566	414	18	5	6105	2	1	f
102517	414	17	6	6104	1	0	t
102467	414	16	6	6103	2	0	t
102468	414	16	7	6103	1	0	t
102518	414	17	7	6104	1	2	t
102519	414	17	8	6104	2	0	t
102520	414	17	9	6104	1	0	t
102569	414	18	8	6105	2	1	t
102528	414	17	17	6104	2	0	t
102527	414	17	16	6104	1	2	t
102570	414	18	9	6105	2	1	t
102529	414	17	18	6104	1	0	t
102478	414	16	17	6103	1	2	t
102546	414	17	35	6104	1	0	t
102479	414	16	18	6103	2	0	f
102530	414	17	19	6104	1	2	t
102539	414	17	28	6104	2	0	t
102480	414	16	19	6103	2	1	t
102540	414	17	29	6104	1	0	t
102446	414	15	35	6102	1	0	f
102490	414	16	29	6103	1	2	t
102496	414	16	35	6103	1	2	t
102447	414	15	36	6102	1	0	t
102497	414	16	36	6103	2	1	t
102448	414	15	37	6102	1	0	t
102547	414	17	36	6104	1	2	t
102449	414	15	38	6102	1	0	t
102557	414	17	46	6104	1	2	t
102498	414	16	37	6103	1	2	t
102450	414	15	39	6102	1	0	t
102549	414	17	38	6104	1	0	t
102459	414	15	48	6102	1	0	t
102458	414	15	47	6102	1	0	t
102559	414	17	48	6104	2	0	t
102650	414	19	39	6106	2	1	t
102750	414	21	39	6108	2	1	t
102710	414	20	49	6107	2	0	t
102610	414	18	49	6105	2	1	f
105259	415	35	48	6158	3	1	f
106737	416	25	26	6188	2	1	t
103498	415	0	37	6123	0	2	f
102671	414	20	10	6107	0	1	t
102673	414	20	12	6107	0	1	t
102721	414	21	10	6108	0	1	t
102672	414	20	11	6107	2	0	t
102631	414	19	20	6106	2	0	t
101782	414	2	21	6089	0	1	t
101781	414	2	20	6089	0	2	t
102691	414	20	30	6107	2	0	t
101681	414	0	20	6087	0	2	t
102632	414	19	21	6106	0	1	t
102692	414	20	31	6107	0	1	t
102741	414	21	30	6108	2	1	t
102700	414	20	39	6107	2	1	f
102642	414	19	31	6106	0	1	f
102643	414	19	32	6106	0	1	t
102651	414	19	40	6106	2	1	f
102701	414	20	40	6107	2	1	f
102751	414	21	40	6108	2	1	f
102702	414	20	41	6107	2	0	t
102703	414	20	42	6107	0	1	t
102752	414	21	41	6108	2	1	f
103500	415	0	39	6123	1	3	t
103502	415	0	41	6123	0	1	t
102722	414	21	11	6108	2	1	t
102624	414	19	13	6106	0	1	t
102623	414	19	12	6106	2	0	t
102675	414	20	14	6107	0	1	t
102674	414	20	13	6107	2	0	t
102382	414	14	21	6101	1	0	t
102633	414	19	22	6106	2	1	t
102634	414	19	23	6106	2	0	t
102744	414	21	33	6108	2	1	t
102684	414	20	23	6107	2	0	t
102635	414	19	24	6106	0	1	t
102693	414	20	32	6107	2	1	t
102644	414	19	33	6106	2	1	t
102694	414	20	33	6107	2	1	f
102645	414	19	34	6106	2	1	t
102602	414	18	41	6105	2	1	f
102652	414	19	41	6106	2	1	f
102603	414	18	42	6105	2	1	f
102704	414	20	43	6107	2	0	f
102705	414	20	44	6107	2	0	t
102625	414	19	14	6106	2	0	f
102676	414	20	15	6107	2	0	t
102725	414	21	14	6108	2	1	t
102626	414	19	15	6106	2	1	t
102686	414	20	25	6107	0	1	t
102685	414	20	24	6107	0	1	f
102737	414	21	26	6108	0	1	f
102736	414	21	25	6108	2	0	t
102636	414	19	25	6106	2	1	f
102696	414	20	35	6107	0	1	t
102745	414	21	34	6108	2	1	f
102746	414	21	35	6108	2	0	t
102698	414	20	37	6107	0	1	f
102646	414	19	35	6106	2	0	t
102654	414	19	43	6106	2	0	f
102604	414	18	43	6105	2	0	f
102605	414	18	44	6105	2	1	f
102706	414	20	45	6107	0	1	t
102655	414	19	44	6106	2	1	f
102677	414	20	16	6107	0	1	f
102678	414	20	17	6107	0	2	f
102613	414	19	2	6106	0	1	t
102612	414	19	1	6106	0	1	f
102727	414	21	16	6108	0	2	t
102663	414	20	2	6107	2	0	f
102614	414	19	3	6106	2	1	f
102665	414	20	4	6107	0	1	t
102615	414	19	4	6106	2	0	f
102666	414	20	5	6107	2	0	t
102616	414	19	5	6106	2	1	t
102667	414	20	6	6107	0	1	t
102617	414	19	6	6106	2	0	t
102668	414	20	7	6107	2	0	t
102618	414	19	7	6106	0	2	t
102669	414	20	8	6107	0	1	t
102670	414	20	9	6107	2	0	t
102619	414	19	8	6106	2	1	f
102728	414	21	17	6108	2	1	f
102679	414	20	18	6107	0	1	f
102620	414	19	9	6106	2	0	t
102687	414	20	26	6107	2	0	t
102629	414	19	18	6106	2	1	f
102680	414	20	19	6107	0	1	t
102738	414	21	27	6108	0	1	t
102747	414	21	36	6108	0	1	t
102630	414	19	19	6106	2	1	t
102690	414	20	29	6107	0	1	t
102688	414	20	27	6107	0	1	f
102689	414	20	28	6107	0	1	f
102707	414	20	46	6107	2	0	t
102739	414	21	28	6108	2	1	f
102697	414	20	36	6107	2	0	t
102740	414	21	29	6108	2	1	f
102748	414	21	37	6108	2	1	f
102699	414	20	38	6107	0	1	t
102606	414	18	45	6105	2	1	f
102749	414	21	38	6108	2	1	f
102657	414	19	46	6106	2	0	f
102708	414	20	47	6107	0	1	t
102709	414	20	48	6107	2	1	t
102658	414	19	47	6106	2	1	f
102609	414	18	48	6105	2	1	t
102760	414	21	49	6108	0	1	t
102860	414	23	49	6110	2	0	t
102810	414	22	49	6109	2	1	f
103659	415	3	48	6126	2	3	t
102471	414	16	10	6103	2	0	f
102781	414	22	20	6109	0	1	t
101921	414	5	10	6092	1	2	t
101922	414	5	11	6092	0	1	t
102791	414	22	30	6109	0	1	t
102881	414	24	20	6111	2	1	f
102732	414	21	21	6108	0	1	t
101682	414	0	21	6087	0	2	t
102883	414	24	22	6111	0	1	f
102782	414	22	21	6109	2	1	t
102841	414	23	30	6110	2	0	t
102842	414	23	31	6110	0	1	t
102901	414	24	40	6111	2	0	t
102892	414	24	31	6111	0	1	f
102851	414	23	40	6110	0	2	t
102902	414	24	41	6111	0	1	t
102903	414	24	42	6111	2	0	t
102802	414	22	41	6109	0	1	t
103505	415	0	44	6123	1	3	f
103507	415	0	46	6123	2	3	t
103508	415	0	47	6123	0	2	t
102472	414	16	11	6103	2	0	t
102873	414	24	12	6111	0	1	t
102823	414	23	12	6110	2	0	t
102824	414	23	13	6110	0	1	t
102775	414	22	14	6109	0	1	f
102884	414	24	23	6111	0	1	t
102833	414	23	22	6110	2	1	f
102885	414	24	24	6111	2	0	t
102834	414	23	23	6110	2	1	f
102843	414	23	32	6110	2	0	t
102844	414	23	33	6110	0	1	t
102893	414	24	32	6111	0	2	f
102894	414	24	33	6111	0	1	f
102794	414	22	33	6109	2	0	t
102853	414	23	42	6110	2	1	f
102754	414	21	43	6108	0	1	t
102803	414	22	42	6109	2	1	f
102805	414	22	44	6109	0	1	t
102904	414	24	43	6111	0	1	f
102874	414	24	13	6111	2	0	t
102776	414	22	15	6109	0	1	t
102875	414	24	14	6111	0	1	f
102825	414	23	14	6110	2	0	t
102827	414	23	16	6110	0	1	t
102835	414	23	24	6110	2	0	t
102836	414	23	25	6110	0	1	t
102786	414	22	25	6109	0	1	t
102838	414	23	27	6110	0	1	t
102886	414	24	25	6111	0	1	f
102787	414	22	26	6109	2	0	t
102895	414	24	34	6111	0	2	t
102845	414	23	34	6110	2	0	t
102846	414	23	35	6110	0	1	t
102796	414	22	35	6109	2	0	t
102797	414	22	36	6109	0	1	f
102896	414	24	35	6111	2	1	f
102848	414	23	37	6110	0	1	t
102854	414	23	43	6110	2	1	t
102905	414	24	44	6111	0	2	t
102806	414	22	45	6109	2	0	t
102755	414	21	44	6108	2	1	f
102876	414	24	15	6111	0	1	f
102863	414	24	2	6111	0	1	t
102762	414	22	1	6109	2	1	f
102864	414	24	3	6111	2	0	t
102763	414	22	2	6109	2	0	f
102828	414	23	17	6110	2	0	t
102865	414	24	4	6111	0	1	t
102765	414	22	4	6109	2	0	t
102766	414	22	5	6109	0	1	f
102877	414	24	16	6111	0	2	t
102866	414	24	5	6111	2	0	t
102767	414	22	6	6109	0	1	t
102867	414	24	6	6111	0	1	t
102869	414	24	8	6111	0	1	t
102868	414	24	7	6111	2	0	t
102768	414	22	7	6109	2	1	f
102769	414	22	8	6109	2	1	f
102770	414	22	9	6109	2	0	f
102837	414	23	26	6110	2	0	t
102870	414	24	9	6111	2	0	f
102878	414	24	17	6111	2	1	t
102829	414	23	18	6110	0	1	f
102879	414	24	18	6111	2	0	t
102830	414	23	19	6110	0	1	t
102847	414	23	36	6110	2	0	t
102880	414	24	19	6111	0	2	t
102788	414	22	27	6109	0	1	t
102839	414	23	28	6110	2	0	t
102840	414	23	29	6110	0	1	t
102789	414	22	28	6109	2	1	f
102790	414	22	29	6109	2	0	t
102798	414	22	37	6109	0	2	t
102849	414	23	38	6110	2	0	t
102900	414	24	39	6111	0	1	t
102799	414	22	38	6109	2	1	t
102757	414	21	46	6108	0	1	t
102850	414	23	39	6110	0	1	f
102856	414	23	45	6110	2	1	f
102808	414	22	47	6109	2	0	t
102807	414	22	46	6109	0	1	t
102857	414	23	46	6110	2	1	t
102758	414	21	47	6108	2	1	f
102809	414	22	48	6109	0	1	t
102759	414	21	48	6108	2	0	t
102859	414	23	48	6110	2	1	f
102910	414	24	49	6111	2	0	t
102960	414	25	49	6112	2	1	t
102931	414	25	20	6112	0	1	f
102071	414	8	10	6095	1	2	t
102932	414	25	21	6112	0	1	t
102021	414	7	10	6094	1	2	t
102981	414	26	20	6113	0	2	t
102991	414	26	30	6113	2	1	t
102933	414	25	22	6112	2	1	t
102882	414	24	21	6111	2	0	t
103033	414	27	22	6114	2	1	t
102600	414	18	39	6105	2	1	f
102941	414	25	30	6112	2	1	f
103042	414	27	31	6114	2	0	t
106140	416	13	29	6176	2	0	t
101842	414	3	31	6090	0	2	t
103051	414	27	40	6114	0	1	t
102951	414	25	40	6112	2	0	t
102952	414	25	41	6112	0	1	t
103053	414	27	42	6114	0	1	t
103052	414	27	41	6114	2	0	t
104225	415	15	14	6138	1	3	t
103660	415	3	49	6126	0	3	f
103513	415	1	2	6124	0	1	t
103515	415	1	4	6124	1	2	t
102072	414	8	11	6095	0	1	t
102022	414	7	11	6094	0	2	t
102973	414	26	12	6113	0	1	t
102923	414	25	12	6112	2	0	t
102924	414	25	13	6112	0	1	t
102984	414	26	23	6113	2	0	t
102934	414	25	23	6112	2	1	f
102985	414	26	24	6113	0	1	t
103034	414	27	23	6114	2	1	f
103036	414	27	25	6114	2	0	t
103393	414	34	32	6121	0	1	t
103043	414	27	32	6114	0	1	t
101893	414	4	32	6091	0	2	t
102994	414	26	33	6113	0	1	t
103044	414	27	33	6114	2	1	f
102945	414	25	34	6112	2	1	f
102953	414	25	42	6112	2	1	t
102955	414	25	44	6112	0	1	t
103003	414	26	42	6113	2	1	t
102954	414	25	43	6112	2	0	t
103054	414	27	43	6114	2	1	f
103516	415	1	5	6124	2	3	f
103023	414	27	12	6114	2	1	t
102935	414	25	24	6112	2	1	f
102974	414	26	13	6113	2	0	t
102975	414	26	14	6113	0	1	f
102926	414	25	15	6112	0	1	t
102925	414	25	14	6112	2	0	t
102927	414	25	16	6112	2	0	t
102936	414	25	25	6112	2	1	t
103037	414	27	26	6114	0	1	t
102986	414	26	25	6113	2	1	t
102937	414	25	26	6112	2	0	t
102938	414	25	27	6112	0	1	f
102995	414	26	34	6113	2	1	f
102946	414	25	35	6112	2	1	t
102996	414	26	35	6113	2	1	t
103047	414	27	36	6114	2	0	t
103005	414	26	44	6113	0	1	f
103006	414	26	45	6113	0	1	t
103057	414	27	46	6114	2	0	f
102956	414	25	45	6112	2	1	f
102976	414	26	15	6113	0	1	t
103062	414	28	1	6115	0	1	t
103013	414	27	2	6114	0	1	t
103026	414	27	15	6114	2	1	f
103063	414	28	2	6115	2	0	t
103064	414	28	3	6115	0	1	t
103014	414	27	3	6114	2	0	f
103015	414	27	4	6114	2	0	t
102965	414	26	4	6113	2	0	f
103016	414	27	5	6114	0	1	t
102915	414	25	4	6112	2	1	t
102928	414	25	17	6112	0	1	t
102916	414	25	5	6112	2	1	f
102977	414	26	16	6113	2	0	t
102917	414	25	6	6112	2	0	t
103017	414	27	6	6114	2	1	t
102918	414	25	7	6112	0	1	t
102969	414	26	8	6113	2	0	t
103018	414	27	7	6114	2	1	f
102970	414	26	9	6113	0	1	t
103019	414	27	8	6114	2	1	t
102939	414	25	28	6112	0	1	f
103020	414	27	9	6114	2	1	t
102978	414	26	17	6113	0	1	f
102979	414	26	18	6113	0	1	f
103038	414	27	27	6114	2	1	t
102929	414	25	18	6112	2	0	t
102930	414	25	19	6112	0	1	f
102980	414	26	19	6113	0	1	f
102990	414	26	29	6113	0	1	t
103039	414	27	28	6114	2	1	f
102997	414	26	36	6113	2	0	t
103048	414	27	37	6114	0	1	t
102940	414	25	29	6112	0	1	t
102947	414	25	36	6112	2	1	f
102998	414	26	37	6113	0	1	f
102999	414	26	38	6113	0	1	t
102949	414	25	38	6112	2	0	t
102950	414	25	39	6112	0	1	t
102957	414	25	46	6112	2	1	f
102958	414	25	47	6112	2	0	t
103007	414	26	46	6113	2	1	f
102959	414	25	48	6112	0	1	t
103058	414	27	47	6114	2	1	f
102909	414	24	48	6111	0	1	t
103071	414	28	10	6115	2	0	t
103171	414	30	10	6117	2	0	t
103081	414	28	20	6115	0	1	f
103182	414	30	21	6117	0	1	t
103131	414	29	20	6116	2	1	f
103183	414	30	22	6117	2	0	t
103082	414	28	21	6115	0	1	t
103091	414	28	30	6115	0	1	t
103200	414	30	39	6117	2	0	t
103191	414	30	30	6117	2	1	f
103092	414	28	31	6115	2	0	t
103201	414	30	40	6117	0	1	t
102792	414	22	31	6109	2	0	t
103110	414	28	49	6115	0	1	t
103102	414	28	41	6115	0	1	t
103101	414	28	40	6115	2	0	t
103210	414	30	49	6117	2	0	t
103103	414	28	42	6115	2	0	t
103152	414	29	41	6116	2	1	t
103160	414	29	49	6116	2	1	f
103625	415	3	14	6126	2	3	t
103519	415	1	8	6124	0	2	f
103072	414	28	11	6115	0	1	t
103121	414	29	10	6116	2	1	t
103172	414	30	11	6117	0	2	t
103073	414	28	12	6115	2	0	t
103122	414	29	11	6116	2	1	f
103084	414	28	23	6115	0	1	t
103083	414	28	22	6115	2	0	t
103184	414	30	23	6117	0	1	f
103185	414	30	24	6117	0	1	f
103093	414	28	32	6115	0	1	t
103194	414	30	33	6117	0	1	f
101843	414	3	32	6090	0	2	t
103095	414	28	34	6115	0	1	t
103094	414	28	33	6115	2	0	t
103202	414	30	41	6117	2	1	f
103204	414	30	43	6117	0	1	f
103153	414	29	42	6116	2	1	t
103521	415	1	10	6124	0	3	f
103104	414	28	43	6115	0	1	f
103205	414	30	44	6117	0	1	t
103173	414	30	12	6117	2	1	f
103074	414	28	13	6115	0	1	f
103124	414	29	13	6116	2	0	t
103125	414	29	14	6116	0	1	f
103174	414	30	13	6117	2	1	t
103134	414	29	23	6116	2	1	t
103086	414	28	25	6115	0	1	t
103085	414	28	24	6115	2	0	t
103187	414	30	26	6117	0	2	t
103186	414	30	25	6117	0	1	f
103096	414	28	35	6115	2	0	t
103195	414	30	34	6117	0	2	t
103145	414	29	34	6116	2	1	f
103196	414	30	35	6117	2	1	f
103106	414	28	45	6115	0	1	t
103105	414	28	44	6115	0	1	f
103207	414	30	46	6117	0	1	t
103206	414	30	45	6117	2	0	t
103156	414	29	45	6116	2	1	t
103075	414	28	14	6115	0	1	f
103088	414	28	27	6115	0	1	f
103076	414	28	15	6115	0	1	t
103077	414	28	16	6115	2	0	t
103126	414	29	15	6116	0	1	t
103078	414	28	17	6115	0	1	t
103127	414	29	16	6116	2	1	f
103162	414	30	1	6117	0	2	t
103213	414	31	2	6118	2	0	t
103178	414	30	17	6117	0	2	t
103163	414	30	2	6117	2	0	f
103214	414	31	3	6118	0	1	f
103215	414	31	4	6118	0	1	t
103079	414	28	18	6115	2	0	t
103115	414	29	4	6116	0	1	f
103117	414	29	6	6116	0	1	t
103216	414	31	5	6118	2	1	f
103128	414	29	17	6116	2	1	t
103217	414	31	6	6118	2	0	t
103067	414	28	6	6115	2	0	f
103218	414	31	7	6118	0	1	t
103068	414	28	7	6115	2	0	t
103118	414	29	7	6116	2	1	t
103069	414	28	8	6115	0	1	f
103219	414	31	8	6118	2	0	t
103087	414	28	26	6115	2	0	t
103169	414	30	8	6117	2	0	t
103070	414	28	9	6115	0	1	t
103220	414	31	9	6118	0	1	f
103179	414	30	18	6117	2	1	f
103080	414	28	19	6115	0	1	f
103130	414	29	19	6116	2	1	t
103089	414	28	28	6115	0	1	t
103138	414	29	27	6116	2	1	t
103188	414	30	27	6117	2	1	f
103190	414	30	29	6117	0	1	t
103139	414	29	28	6116	2	1	f
103097	414	28	36	6115	0	1	t
103090	414	28	29	6115	2	0	t
103098	414	28	37	6115	2	0	t
103197	414	30	36	6117	2	0	f
103199	414	30	38	6117	0	1	t
103198	414	30	37	6117	2	0	t
103100	414	28	39	6115	0	1	t
103099	414	28	38	6115	0	1	f
103107	414	28	46	6115	2	0	t
103108	414	28	47	6115	0	1	t
103209	414	30	48	6117	0	1	t
103208	414	30	47	6117	2	0	t
103109	414	28	48	6115	2	0	t
103331	414	33	20	6120	0	2	t
103231	414	31	20	6118	2	1	f
103232	414	31	21	6118	2	0	t
103233	414	31	22	6118	0	1	t
103282	414	32	21	6119	2	1	t
103241	414	31	30	6118	0	1	t
103250	414	31	39	6118	0	2	f
103341	414	33	30	6120	0	2	t
103251	414	31	40	6118	0	1	t
103000	414	26	39	6113	2	1	f
103242	414	31	31	6118	2	0	f
103192	414	30	31	6117	2	0	f
103360	414	33	49	6120	0	1	t
103400	414	34	39	6121	2	1	f
103252	414	31	41	6118	2	1	t
103001	414	26	40	6113	2	1	t
103260	414	31	49	6118	2	1	f
103253	414	31	42	6118	2	0	t
103310	414	32	49	6119	2	1	f
104592	415	22	31	6145	2	1	t
105242	415	35	31	6158	3	1	t
103626	415	3	15	6126	0	1	t
103524	415	1	13	6124	1	3	t
103221	414	31	10	6118	0	1	t
103222	414	31	11	6118	2	0	t
103371	414	34	10	6121	0	1	t
103321	414	33	10	6120	2	1	t
103373	414	34	12	6121	0	1	t
103372	414	34	11	6121	2	0	t
103334	414	33	23	6120	0	1	f
103283	414	32	22	6119	2	1	t
103302	414	32	41	6119	2	1	f
103335	414	33	24	6120	0	1	t
103234	414	31	23	6118	2	0	t
102793	414	22	32	6109	0	1	t
103193	414	30	32	6117	2	0	t
103243	414	31	32	6118	2	1	f
103344	414	33	33	6120	0	2	t
103245	414	31	34	6118	0	1	t
103244	414	31	33	6118	2	0	t
103254	414	31	43	6118	0	1	f
103303	414	32	42	6119	2	1	f
103304	414	32	43	6119	2	1	t
103223	414	31	12	6118	0	1	t
103374	414	34	13	6121	2	0	t
103273	414	32	12	6119	2	1	t
103236	414	31	25	6118	0	1	f
103235	414	31	24	6118	0	1	f
103285	414	32	24	6119	2	1	f
103336	414	33	25	6120	2	0	t
103337	414	33	26	6120	0	1	t
103255	414	31	44	6118	0	2	t
103295	414	32	34	6119	2	1	t
103345	414	33	34	6120	2	1	f
103246	414	31	35	6118	2	1	t
103296	414	32	35	6119	2	1	f
103347	414	33	36	6120	0	2	t
103306	414	32	45	6119	2	0	t
103305	414	32	44	6119	2	1	t
103256	414	31	45	6118	2	1	f
103356	414	33	45	6120	2	1	f
103224	414	31	13	6118	2	1	f
103375	414	34	14	6121	0	1	f
103225	414	31	14	6118	2	1	t
103376	414	34	15	6121	0	2	t
103275	414	32	14	6119	2	1	f
103238	414	31	27	6118	0	2	t
103237	414	31	26	6118	0	1	f
103339	414	33	28	6120	0	2	t
103226	414	31	15	6118	2	0	t
103313	414	33	2	6120	2	0	f
103362	414	34	1	6121	2	1	f
103327	414	33	16	6120	0	1	t
103315	414	33	4	6120	2	0	f
103363	414	34	2	6121	2	0	f
103314	414	33	3	6120	2	1	f
103365	414	34	4	6121	2	1	f
103366	414	34	5	6121	2	0	t
103367	414	34	6	6121	0	1	t
103316	414	33	5	6120	2	1	f
103276	414	32	15	6119	2	1	t
103368	414	34	7	6121	2	0	t
103267	414	32	6	6119	2	1	t
103268	414	32	7	6119	2	1	t
103319	414	33	8	6120	0	1	t
103369	414	34	8	6121	0	1	t
103370	414	34	9	6121	2	0	t
103228	414	31	17	6118	0	1	t
103320	414	33	9	6120	2	0	f
103227	414	31	16	6118	0	1	f
103277	414	32	16	6119	2	1	f
103329	414	33	18	6120	0	2	t
103328	414	33	17	6120	2	0	t
103278	414	32	17	6119	2	1	t
103229	414	31	18	6118	2	0	t
103230	414	31	19	6118	0	1	t
103338	414	33	27	6120	2	0	t
103330	414	33	19	6120	2	0	t
103289	414	32	28	6119	2	1	t
103240	414	31	29	6118	2	0	t
103248	414	31	37	6118	2	0	t
103247	414	31	36	6118	2	0	f
103340	414	33	29	6120	2	0	t
103249	414	31	38	6118	0	1	f
103348	414	33	37	6120	2	1	f
103299	414	32	38	6119	2	1	t
103257	414	31	46	6118	2	0	t
103307	414	32	46	6119	0	2	t
103258	414	31	47	6118	0	1	t
103358	414	33	47	6120	0	1	t
103359	414	33	48	6120	2	0	t
103259	414	31	48	6118	2	1	f
103431	414	35	20	6122	2	1	f
103432	414	35	21	6122	2	0	t
103441	414	35	30	6122	2	0	t
103442	414	35	31	6122	0	1	t
103392	414	34	31	6121	2	0	t
103443	414	35	32	6122	2	0	t
103444	414	35	33	6122	0	1	f
103451	414	35	40	6122	2	1	t
103402	414	34	41	6121	0	1	f
103404	414	34	43	6121	0	1	t
103452	414	35	41	6122	2	0	t
103403	414	34	42	6121	0	1	f
103460	414	35	49	6122	2	1	f
103410	414	34	49	6121	2	1	f
104842	415	27	31	6150	3	1	t
105009	415	30	48	6153	3	2	f
103529	415	1	18	6124	0	2	t
103421	414	35	10	6122	2	1	t
102872	414	24	11	6111	2	0	t
102521	414	17	10	6104	1	2	t
103021	414	27	10	6114	2	1	t
103381	414	34	20	6121	2	1	f
102921	414	25	10	6112	2	1	f
102831	414	23	20	6110	2	1	f
102821	414	23	10	6110	2	1	f
103433	414	35	22	6122	0	1	f
103382	414	34	21	6121	2	1	t
103434	414	35	23	6122	0	2	t
103435	414	35	24	6122	2	1	f
103384	414	34	23	6121	2	1	t
103446	414	35	35	6122	0	1	t
103394	414	34	33	6121	2	0	t
103445	414	35	34	6122	0	1	f
103396	414	34	35	6121	2	1	f
103447	414	35	36	6122	2	1	t
103456	414	35	45	6122	0	1	t
103454	414	35	43	6122	2	0	t
103405	414	34	44	6121	2	1	t
103406	414	34	45	6121	2	1	f
103436	414	35	25	6122	2	0	t
102871	414	24	10	6111	2	1	f
102771	414	22	10	6109	2	1	f
102161	414	10	0	6097	1	0	t
101761	414	2	0	6089	0	1	t
102311	414	13	0	6100	1	0	t
102061	414	8	0	6095	0	1	t
102211	414	11	0	6098	1	0	t
101711	414	1	0	6088	0	1	t
103437	414	35	26	6122	0	1	t
102411	414	15	0	6102	1	0	t
101911	414	5	0	6092	0	1	t
101861	414	4	0	6091	0	1	f
103386	414	34	25	6121	2	1	f
102611	414	19	0	6106	2	0	t
101811	414	3	0	6090	0	2	t
102661	414	20	0	6107	2	0	t
101661	414	0	0	6087	0	2	t
103388	414	34	27	6121	0	1	f
103161	414	30	0	6117	2	0	t
101961	414	6	0	6093	0	2	t
103061	414	28	0	6115	2	0	t
102011	414	7	0	6094	0	2	t
103389	414	34	28	6121	0	1	t
102111	414	9	0	6096	1	2	t
103211	414	31	0	6118	2	1	t
103438	414	35	27	6122	2	0	t
103424	414	35	13	6122	0	1	t
102261	414	12	0	6099	1	2	t
102961	414	26	0	6113	2	1	t
103425	414	35	14	6122	2	1	f
102361	414	14	0	6101	1	2	t
102761	414	22	0	6109	2	1	t
102511	414	17	0	6104	1	2	t
102811	414	23	0	6110	2	1	t
103426	414	35	15	6122	2	0	t
102461	414	16	0	6103	1	2	t
103361	414	34	0	6121	2	1	t
103111	414	29	0	6116	2	1	f
103427	414	35	16	6122	0	1	t
103428	414	35	17	6122	2	0	t
103377	414	34	16	6121	2	1	f
102662	414	20	1	6107	0	1	t
102212	414	11	1	6098	1	0	t
101812	414	3	1	6090	0	1	t
102412	414	15	1	6102	1	0	t
101962	414	6	1	6093	0	1	t
102362	414	14	1	6101	2	0	t
101662	414	0	1	6087	0	2	t
101862	414	4	1	6091	0	2	t
102012	414	7	1	6094	0	2	t
102462	414	16	1	6103	2	0	t
102262	414	12	1	6099	2	0	f
103415	414	35	4	6122	2	1	t
103414	414	35	3	6122	0	2	t
103416	414	35	5	6122	2	1	f
103417	414	35	6	6122	2	0	t
103418	414	35	7	6122	0	2	t
103419	414	35	8	6122	2	1	t
103420	414	35	9	6122	2	1	t
103429	414	35	18	6122	0	1	t
103378	414	34	17	6121	2	1	t
103380	414	34	19	6121	2	1	t
103379	414	34	18	6121	2	1	f
103430	414	35	19	6122	2	1	t
103440	414	35	29	6122	0	1	t
103398	414	34	37	6121	0	1	f
103390	414	34	29	6121	2	1	f
103399	414	34	38	6121	0	1	t
103448	414	35	37	6122	2	1	f
103450	414	35	39	6122	0	1	t
103457	414	35	46	6122	2	1	t
103408	414	34	47	6121	2	1	t
103458	414	35	47	6122	2	1	f
103409	414	34	48	6121	2	1	f
102971	414	26	10	6113	2	1	f
102561	414	18	0	6105	2	1	f
103292	414	32	31	6119	2	1	t
103411	414	35	0	6122	2	1	f
102571	414	18	10	6105	2	1	f
103011	414	27	0	6114	2	1	f
102681	414	20	20	6107	2	1	f
102911	414	25	0	6112	2	1	f
103311	414	33	0	6120	2	1	f
103261	414	32	0	6119	2	1	f
102972	414	26	11	6113	2	0	t
102711	414	21	0	6108	2	1	f
102572	414	18	11	6105	2	1	f
102861	414	24	0	6111	2	1	f
102023	414	7	12	6094	0	2	t
102862	414	24	1	6111	2	0	t
103012	414	27	1	6114	2	0	t
103312	414	33	1	6120	2	0	f
102812	414	23	1	6110	2	0	f
102912	414	25	1	6112	2	0	f
102112	414	9	1	6096	2	0	f
102712	414	21	1	6108	2	1	t
103112	414	29	1	6116	2	1	t
103262	414	32	1	6119	2	1	t
101712	414	1	1	6088	1	2	t
102562	414	18	1	6105	2	1	t
102962	414	26	1	6113	2	1	f
103212	414	31	1	6118	2	1	f
103412	414	35	1	6122	2	1	f
102273	414	12	12	6099	2	0	f
102363	414	14	2	6101	1	0	t
101713	414	1	2	6088	0	2	t
103413	414	35	2	6122	2	0	t
102913	414	25	2	6112	2	0	f
102024	414	7	13	6094	0	2	t
102713	414	21	2	6108	2	0	f
101813	414	3	2	6090	1	2	t
102113	414	9	2	6096	2	1	t
101963	414	6	2	6093	1	2	t
103263	414	32	2	6119	2	1	t
102213	414	11	2	6098	1	2	t
102463	414	16	2	6103	1	2	t
102813	414	23	2	6110	2	1	t
102963	414	26	2	6113	2	1	f
103113	414	29	2	6116	2	1	f
102064	414	8	3	6095	0	1	t
102314	414	13	3	6100	1	0	t
101714	414	1	3	6088	0	1	t
102114	414	9	3	6096	1	0	t
102664	414	20	3	6107	2	0	t
101964	414	6	3	6093	0	2	t
101814	414	3	3	6090	0	2	t
103114	414	29	3	6116	2	0	t
101864	414	4	3	6091	0	2	t
102264	414	12	3	6099	2	0	t
102464	414	16	3	6103	2	0	f
102714	414	21	3	6108	2	0	f
102214	414	11	3	6098	2	0	f
102914	414	25	3	6112	2	1	t
102364	414	14	3	6101	1	2	t
102764	414	22	3	6109	2	1	t
103264	414	32	3	6119	2	1	f
102964	414	26	3	6113	2	1	f
102564	414	18	3	6105	2	1	f
103364	414	34	3	6121	2	1	f
103164	414	30	3	6117	2	1	f
102814	414	23	3	6110	2	1	f
103065	414	28	4	6115	2	0	f
101715	414	1	4	6088	1	2	t
101915	414	5	4	6092	1	2	t
102065	414	8	4	6095	1	2	t
102715	414	21	4	6108	2	1	t
102265	414	12	4	6099	1	2	t
102515	414	17	4	6104	1	2	t
103165	414	30	4	6117	2	1	t
102365	414	14	4	6101	2	1	f
103265	414	32	4	6119	2	1	f
102815	414	23	4	6110	2	1	f
101916	414	5	5	6092	0	1	t
102066	414	8	5	6095	0	1	t
101766	414	2	5	6089	0	1	t
103116	414	29	5	6116	0	1	f
102516	414	17	5	6104	2	0	t
101716	414	1	5	6088	0	2	t
102816	414	23	5	6110	2	0	t
102366	414	14	5	6101	2	0	f
102266	414	12	5	6099	2	0	f
103166	414	30	5	6117	2	1	t
102716	414	21	5	6108	2	1	t
103266	414	32	5	6119	2	1	f
102966	414	26	5	6113	2	1	f
103066	414	28	5	6115	2	1	f
102817	414	23	6	6110	0	1	f
101817	414	3	6	6090	0	2	t
101917	414	5	6	6092	1	2	t
102717	414	21	6	6108	2	1	t
102067	414	8	6	6095	1	2	t
103317	414	33	6	6120	2	1	f
102217	414	11	6	6098	2	1	f
102367	414	14	6	6101	2	1	f
103167	414	30	6	6117	2	1	f
102967	414	26	6	6113	2	1	f
102567	414	18	6	6105	2	1	f
102818	414	23	7	6110	0	1	t
101918	414	5	7	6092	0	1	t
102068	414	8	7	6095	0	1	t
103318	414	33	7	6120	2	0	t
102218	414	11	7	6098	2	0	t
102368	414	14	7	6101	2	0	t
101868	414	4	7	6091	0	2	f
102968	414	26	7	6113	2	1	f
101669	414	0	8	6087	0	2	t
101869	414	4	8	6091	0	2	t
103168	414	30	7	6117	2	1	f
102718	414	21	7	6108	2	1	f
102568	414	18	7	6105	2	1	f
102419	414	15	8	6102	1	0	t
102269	414	12	8	6099	2	0	t
101771	414	2	10	6089	0	2	t
103271	414	32	10	6119	2	1	f
102069	414	8	8	6095	1	2	t
102522	414	17	11	6104	2	0	t
102469	414	16	8	6103	1	2	t
103119	414	29	8	6116	2	1	f
102272	414	12	11	6099	1	2	t
102919	414	25	8	6112	2	1	f
102772	414	22	11	6109	2	1	t
102719	414	21	8	6108	2	1	f
103422	414	35	11	6122	2	1	f
102819	414	23	8	6110	2	1	f
103269	414	32	8	6119	2	1	f
102922	414	25	11	6112	2	1	f
101920	414	5	9	6092	0	1	t
103170	414	30	9	6117	0	1	t
102070	414	8	9	6095	0	1	t
102420	414	15	9	6102	1	0	t
102720	414	21	9	6108	2	0	t
101870	414	4	9	6091	0	2	t
102820	414	23	9	6110	2	0	f
102920	414	25	9	6112	2	0	f
102470	414	16	9	6103	2	0	f
101770	414	2	9	6089	1	2	t
102381	414	14	20	6101	2	0	t
102270	414	12	9	6099	1	2	t
103270	414	32	9	6119	2	1	t
103281	414	32	20	6119	2	1	f
103120	414	29	9	6116	2	1	f
102581	414	18	20	6105	2	1	f
103022	414	27	11	6114	2	1	f
105042	415	31	31	6154	3	2	t
102822	414	23	11	6110	2	1	f
103322	414	33	11	6120	2	1	f
103272	414	32	11	6119	2	1	f
103423	414	35	12	6122	2	0	t
101673	414	0	12	6087	0	2	t
102573	414	18	12	6105	2	1	t
102073	414	8	12	6095	1	2	t
102723	414	21	12	6108	2	1	t
102373	414	14	12	6101	1	2	t
102682	414	20	21	6107	2	0	t
102582	414	18	21	6105	2	1	t
103323	414	33	12	6120	2	1	t
101983	414	6	22	6093	0	2	t
103123	414	29	12	6116	2	1	f
102773	414	22	12	6109	2	1	f
102074	414	8	13	6095	0	1	f
102774	414	22	13	6109	2	0	t
101774	414	2	13	6089	0	2	t
102274	414	12	13	6099	2	0	f
102374	414	14	13	6101	2	0	f
103324	414	33	13	6120	2	0	f
103274	414	32	13	6119	2	1	t
102574	414	18	13	6105	2	1	f
102724	414	21	13	6108	2	1	f
103024	414	27	13	6114	2	1	f
101675	414	0	14	6087	0	2	t
102233	414	11	22	6098	1	2	t
102125	414	9	14	6096	2	1	f
103025	414	27	14	6114	2	1	f
103325	414	33	14	6120	2	1	f
103175	414	30	14	6117	2	1	f
102376	414	14	15	6101	1	0	t
102826	414	23	15	6110	0	1	f
102726	414	21	15	6108	2	0	t
102226	414	11	15	6098	2	0	t
101876	414	4	15	6091	0	2	t
102126	414	9	15	6096	2	0	t
101676	414	0	15	6087	0	2	t
103326	414	33	15	6120	2	0	t
102476	414	16	15	6103	2	0	f
103176	414	30	15	6117	2	1	f
102277	414	12	16	6099	2	0	t
102027	414	7	16	6094	0	2	t
103177	414	30	16	6117	2	0	t
101777	414	2	16	6089	0	2	f
102377	414	14	16	6101	1	2	t
102627	414	19	16	6106	2	1	t
103027	414	27	16	6114	2	1	t
102577	414	18	16	6105	2	1	f
102777	414	22	16	6109	2	1	f
101778	414	2	17	6089	0	1	f
102028	414	7	17	6094	0	1	f
101828	414	3	17	6090	0	1	f
102378	414	14	17	6101	2	0	t
102578	414	18	17	6105	2	1	t
102778	414	22	17	6109	2	1	t
102278	414	12	17	6099	1	2	t
103028	414	27	17	6114	2	1	f
102628	414	19	17	6106	2	1	f
102229	414	11	18	6098	2	0	t
102279	414	12	18	6099	2	0	t
101879	414	4	18	6091	0	2	t
102329	414	13	18	6100	2	0	f
102779	414	22	18	6109	2	0	f
102579	414	18	18	6105	2	1	f
103029	414	27	18	6114	2	1	f
103129	414	29	18	6116	2	1	f
103279	414	32	18	6119	2	1	f
102729	414	21	18	6108	2	1	f
102780	414	22	19	6109	2	0	t
101830	414	3	19	6090	0	2	t
101680	414	0	19	6087	0	2	f
101880	414	4	19	6091	0	2	f
102030	414	7	19	6094	1	2	t
102380	414	14	19	6101	1	2	t
103280	414	32	19	6119	2	1	t
102580	414	18	19	6105	2	1	t
102230	414	11	19	6098	1	2	t
102280	414	12	19	6099	1	2	t
103180	414	30	19	6117	2	1	t
103030	414	27	19	6114	2	1	f
102730	414	21	19	6108	2	1	f
102731	414	21	20	6108	2	0	t
103181	414	30	20	6117	2	0	t
103031	414	27	20	6114	2	1	f
101832	414	3	21	6090	0	2	t
102832	414	23	21	6110	2	0	f
103032	414	27	21	6114	2	0	f
103332	414	33	21	6120	2	1	t
103132	414	29	21	6116	2	1	t
102191	414	10	30	6097	1	0	t
102982	414	26	21	6113	2	1	f
102641	414	19	30	6106	2	0	t
102433	414	15	22	6102	1	0	t
102683	414	20	22	6107	0	1	t
101933	414	5	22	6092	0	1	f
103333	414	33	22	6120	2	0	t
101891	414	4	30	6091	0	2	t
103383	414	34	22	6121	2	1	t
102983	414	26	22	6113	2	1	f
103133	414	29	22	6116	2	1	f
102891	414	24	30	6111	2	0	t
102783	414	22	22	6109	2	1	f
102733	414	21	22	6108	2	1	f
101884	414	4	23	6091	0	2	t
101784	414	2	23	6089	0	2	t
102734	414	21	23	6108	2	0	t
102491	414	16	30	6103	2	0	t
101984	414	6	23	6093	0	2	t
102234	414	11	23	6098	2	0	t
102584	414	18	23	6105	2	1	t
103291	414	32	30	6119	2	1	t
102391	414	14	30	6101	1	2	t
103141	414	29	30	6116	2	1	f
102384	414	14	23	6101	2	1	f
103391	414	34	30	6121	2	1	f
103284	414	32	23	6119	2	1	f
103041	414	27	30	6114	2	1	f
102784	414	22	23	6109	2	1	f
102742	414	21	31	6108	2	1	t
102735	414	21	24	6108	0	2	t
102285	414	12	24	6099	2	0	t
102800	414	22	39	6109	2	1	f
102785	414	22	24	6109	2	0	t
102385	414	14	24	6101	2	0	t
101685	414	0	24	6087	0	2	t
102242	414	11	31	6098	1	2	t
103142	414	29	31	6116	2	1	t
102535	414	17	24	6104	1	2	t
103135	414	29	24	6116	2	1	t
103592	415	2	31	6125	2	3	f
103035	414	27	24	6114	2	1	f
102350	414	13	39	6100	2	1	f
103385	414	34	24	6121	2	1	f
101936	414	5	25	6092	0	1	t
102292	414	12	31	6099	1	2	t
102942	414	25	31	6112	2	1	t
102536	414	17	25	6104	2	0	t
101686	414	0	25	6087	0	2	t
101986	414	6	25	6093	0	2	f
103136	414	29	25	6116	2	1	t
103300	414	32	39	6119	2	1	f
102992	414	26	31	6113	2	1	t
102286	414	12	25	6099	1	2	t
103286	414	32	25	6119	2	1	t
102592	414	18	31	6105	2	1	f
102437	414	15	26	6102	1	0	t
102887	414	24	26	6111	0	1	t
102287	414	12	26	6099	2	0	t
102237	414	11	26	6098	2	0	t
103387	414	34	26	6121	2	0	t
101987	414	6	26	6093	0	2	t
101937	414	5	26	6092	1	2	t
103287	414	32	26	6119	2	1	t
102293	414	12	32	6099	2	0	t
102637	414	19	26	6106	2	1	f
103137	414	29	26	6116	2	1	f
102987	414	26	26	6113	2	1	f
102138	414	9	27	6096	1	0	t
101938	414	5	27	6092	0	1	t
102638	414	19	27	6106	2	0	t
102888	414	24	27	6111	2	0	t
101738	414	1	27	6088	0	2	t
101988	414	6	27	6093	0	2	f
102288	414	12	27	6099	1	2	t
102988	414	26	27	6113	2	1	t
102588	414	18	27	6105	2	1	t
103288	414	32	27	6119	2	1	f
102889	414	24	28	6111	0	1	t
102139	414	9	28	6096	1	0	t
102639	414	19	28	6106	0	1	t
103439	414	35	28	6122	0	1	f
102289	414	12	28	6099	2	0	t
102989	414	26	28	6113	2	0	t
103189	414	30	28	6117	2	0	t
101789	414	2	28	6089	1	2	t
101939	414	5	28	6092	1	2	t
102589	414	18	28	6105	2	1	t
103239	414	31	28	6118	2	1	t
102190	414	10	29	6097	1	0	t
102390	414	14	29	6101	2	0	t
101890	414	4	29	6091	0	2	t
101790	414	2	29	6089	0	2	t
101990	414	6	29	6093	0	2	f
101740	414	1	29	6088	0	2	f
102590	414	18	29	6105	2	1	t
103140	414	29	29	6116	2	1	t
103290	414	32	29	6119	2	1	f
102640	414	19	29	6106	2	1	f
103040	414	27	29	6114	2	1	f
102890	414	24	29	6111	2	1	f
101750	414	1	39	6088	0	2	t
103342	414	33	31	6120	2	1	f
103050	414	27	39	6114	2	0	t
102993	414	26	32	6113	2	0	t
103343	414	33	32	6120	2	0	t
102043	414	7	32	6094	0	2	t
102500	414	16	39	6103	1	2	t
101743	414	1	32	6088	0	2	f
103150	414	29	39	6116	2	1	f
102393	414	14	32	6101	1	2	t
102243	414	11	32	6098	2	1	f
102943	414	25	32	6112	2	1	f
103350	414	33	39	6120	2	1	f
102593	414	18	32	6105	2	1	f
103293	414	32	32	6119	2	1	f
102743	414	21	32	6108	2	1	f
103143	414	29	32	6116	2	1	f
102244	414	11	33	6098	2	0	t
101744	414	1	33	6088	0	2	t
102044	414	7	33	6094	0	2	f
103144	414	29	33	6116	2	1	t
102251	414	11	40	6098	1	0	t
102594	414	18	33	6105	2	1	f
103294	414	32	33	6119	2	1	f
102944	414	25	33	6112	2	1	f
101701	414	0	40	6087	0	2	t
102795	414	22	34	6109	0	1	t
103395	414	34	34	6121	0	1	t
102245	414	11	34	6098	1	0	t
102295	414	12	34	6099	2	0	t
102695	414	20	34	6107	2	0	t
101845	414	3	34	6090	0	2	f
103401	414	34	40	6121	2	0	t
102595	414	18	34	6105	2	1	f
102801	414	22	40	6109	2	0	t
105445	415	39	34	6162	3	0	t
102101	414	8	40	6095	1	2	t
103045	414	27	34	6114	2	1	f
102501	414	16	40	6103	2	1	t
101796	414	2	35	6089	0	2	t
101996	414	6	35	6093	0	2	t
103346	414	33	35	6120	2	0	t
103351	414	33	40	6120	2	1	t
102596	414	18	35	6105	2	1	t
102601	414	18	40	6105	2	1	f
103146	414	29	35	6116	2	1	f
103301	414	32	40	6119	2	1	f
103151	414	29	40	6116	2	1	f
103046	414	27	35	6114	2	1	f
102647	414	19	36	6106	0	1	t
102197	414	10	36	6097	1	0	t
101697	414	0	36	6087	0	2	t
103397	414	34	36	6121	2	0	t
101997	414	6	36	6093	0	2	t
101897	414	4	36	6091	0	2	t
102297	414	12	36	6099	2	0	t
102897	414	24	36	6111	2	0	f
103147	414	29	36	6116	2	1	t
103297	414	32	36	6119	2	1	t
102597	414	18	36	6105	2	1	f
102248	414	11	37	6098	1	0	t
102102	414	8	41	6095	0	1	t
101698	414	0	37	6087	0	2	t
101998	414	6	37	6093	0	2	t
102548	414	17	37	6104	2	0	t
101848	414	3	37	6090	0	2	t
101702	414	0	41	6087	0	2	t
103298	414	32	37	6119	2	1	t
102298	414	12	37	6099	1	2	t
103148	414	29	37	6116	2	1	t
103536	415	1	25	6124	2	3	t
102898	414	24	37	6111	2	1	t
102402	414	14	41	6101	2	0	t
102648	414	19	37	6106	2	1	f
102052	414	7	41	6094	0	2	t
102948	414	25	37	6112	2	1	f
102598	414	18	37	6105	2	1	f
102852	414	23	41	6110	2	1	t
102249	414	11	38	6098	1	0	t
102499	414	16	38	6103	2	0	t
103538	415	1	27	6124	0	2	t
103449	414	35	38	6122	2	0	t
101749	414	1	38	6088	0	2	t
102502	414	16	41	6103	1	2	t
102299	414	12	38	6099	2	0	t
102899	414	24	38	6111	2	0	t
101849	414	3	38	6090	0	2	t
102649	414	19	38	6106	2	1	t
102099	414	8	38	6095	1	2	t
103149	414	29	38	6116	2	1	t
103540	415	1	29	6124	0	3	f
103049	414	27	38	6114	2	1	f
103002	414	26	41	6113	2	1	f
103349	414	33	38	6120	2	1	f
103352	414	33	41	6120	2	1	f
102599	414	18	38	6105	2	1	f
102250	414	11	39	6098	1	0	t
102100	414	8	39	6095	0	1	t
103541	415	1	30	6124	0	3	t
103453	414	35	42	6122	0	1	t
101903	414	4	42	6091	0	2	t
102253	414	11	42	6098	2	0	t
102753	414	21	42	6108	2	0	t
103203	414	30	42	6117	2	0	t
101803	414	2	42	6089	0	2	t
102653	414	19	42	6106	2	1	t
102303	414	12	42	6099	1	2	t
103353	414	33	42	6120	2	1	f
101804	414	2	43	6089	0	1	t
102104	414	8	43	6095	0	1	t
102804	414	22	43	6109	2	0	t
103004	414	26	43	6113	2	0	t
102304	414	12	43	6099	2	0	t
103455	414	35	44	6122	0	1	f
102554	414	17	43	6104	2	0	f
101954	414	5	43	6092	1	2	t
102110	414	8	49	6095	0	1	t
101760	414	1	49	6088	0	2	t
102254	414	11	43	6098	1	2	t
103154	414	29	43	6116	2	1	t
102510	414	16	49	6103	2	0	f
102410	414	14	49	6101	2	0	f
103354	414	33	43	6120	2	1	f
103060	414	27	49	6114	2	1	f
101955	414	5	44	6092	0	1	t
102255	414	11	44	6098	2	0	t
103010	414	26	49	6113	2	1	f
102660	414	19	49	6106	2	1	f
103155	414	29	44	6116	2	1	t
103542	415	1	31	6124	0	2	t
102855	414	23	44	6110	2	1	f
103559	415	1	48	6124	2	3	t
102505	414	16	44	6103	2	1	f
103560	415	1	49	6124	0	3	f
103055	414	27	44	6114	2	1	f
103355	414	33	44	6120	2	1	f
109019	417	41	8	6234	3	0	t
102106	414	8	45	6095	0	1	t
101806	414	2	45	6089	0	2	t
102306	414	12	45	6099	2	0	t
102756	414	21	45	6108	2	0	t
102656	414	19	45	6106	2	1	t
103056	414	27	45	6114	2	1	f
102906	414	24	45	6111	2	1	f
102506	414	16	45	6103	2	1	f
101957	414	5	46	6092	0	1	t
103357	414	33	46	6120	2	0	t
101707	414	0	46	6087	0	2	t
102257	414	11	46	6098	2	0	t
102107	414	8	46	6095	1	2	t
103407	414	34	46	6121	2	1	t
102407	414	14	46	6101	1	2	t
102607	414	18	46	6105	2	1	t
103157	414	29	46	6116	2	1	f
102907	414	24	46	6111	2	1	f
102208	414	10	47	6097	1	0	t
102108	414	8	47	6095	0	1	t
102908	414	24	47	6111	2	0	t
101708	414	0	47	6087	0	2	t
102408	414	14	47	6101	2	0	f
102558	414	17	47	6104	2	0	f
103008	414	26	47	6113	2	1	t
101958	414	5	47	6092	1	2	t
103575	415	2	14	6125	0	2	t
102858	414	23	47	6110	2	1	f
103308	414	32	47	6119	2	1	f
103576	415	2	15	6125	2	3	t
103158	414	29	47	6116	2	1	f
103578	415	2	17	6125	2	3	t
102608	414	18	47	6105	2	1	f
101959	414	5	48	6092	0	1	t
101759	414	1	48	6088	0	2	f
102109	414	8	48	6095	1	2	t
103579	415	2	18	6125	0	2	t
103059	414	27	48	6114	2	1	t
102509	414	16	48	6103	1	2	t
103009	414	26	48	6113	2	1	t
103580	415	2	19	6125	2	3	t
102209	414	10	48	6097	1	2	t
103309	414	32	48	6119	2	1	f
102659	414	19	48	6106	2	1	f
103582	415	2	21	6125	2	3	t
103159	414	29	48	6116	2	1	f
103459	414	35	48	6122	2	1	f
102409	414	14	48	6101	2	1	f
103583	415	2	22	6125	0	2	t
104343	415	17	32	6140	1	0	f
103594	415	2	33	6125	0	2	t
103695	415	4	34	6127	0	3	f
103745	415	5	34	6128	0	3	f
103945	415	9	34	6132	0	3	f
105446	415	39	35	6162	0	2	f
103598	415	2	37	6125	0	2	f
103548	415	1	37	6124	0	3	t
103561	415	2	0	6125	0	2	t
103562	415	2	1	6125	2	3	t
103563	415	2	2	6125	0	1	t
103564	415	2	3	6125	1	3	f
103565	415	2	4	6125	1	2	t
103566	415	2	5	6125	2	3	f
103567	415	2	6	6125	2	3	t
103568	415	2	7	6125	0	3	f
103569	415	2	8	6125	0	2	f
103570	415	2	9	6125	0	1	f
103571	415	2	10	6125	0	2	t
103572	415	2	11	6125	2	3	t
103573	415	2	12	6125	0	2	t
103574	415	2	13	6125	2	3	t
103584	415	2	23	6125	2	3	t
103586	415	2	25	6125	2	3	t
103587	415	2	26	6125	0	2	t
103589	415	2	28	6125	0	2	t
103590	415	2	29	6125	2	3	t
103599	415	2	38	6125	0	1	t
103549	415	1	38	6124	0	3	f
103600	415	2	39	6125	1	3	t
103601	415	2	40	6125	0	1	t
103552	415	1	41	6124	0	3	f
103554	415	1	43	6124	0	2	t
103602	415	2	41	6125	1	3	t
103553	415	1	42	6124	0	3	t
103556	415	1	45	6124	0	3	f
103555	415	1	44	6124	2	3	t
103557	415	1	46	6124	0	3	f
103606	415	2	45	6125	1	3	t
103558	415	1	47	6124	0	2	t
103609	415	2	48	6125	0	1	t
106738	416	25	27	6188	2	1	f
103692	415	4	31	6127	0	3	t
103725	415	5	14	6128	0	3	t
103675	415	4	14	6127	0	3	t
103676	415	4	15	6127	0	3	t
103677	415	4	16	6127	0	3	t
103726	415	5	15	6128	0	3	t
103728	415	5	17	6128	0	3	t
103743	415	5	32	6128	0	3	t
103642	415	3	31	6126	1	3	t
103760	415	5	49	6128	0	3	f
103742	415	5	31	6128	1	3	t
103643	415	3	32	6126	0	3	f
103644	415	3	33	6126	0	2	t
103709	415	4	48	6127	0	1	t
104144	415	13	33	6136	3	0	t
103744	415	5	33	6128	0	3	t
109619	417	53	8	6246	0	3	f
103610	415	2	49	6125	1	3	t
103710	415	4	49	6127	1	3	f
107142	417	3	31	6196	0	3	f
106790	416	26	29	6189	2	1	t
106240	416	15	29	6178	2	1	f
105741	416	5	30	6168	0	2	t
103727	415	5	16	6128	0	3	f
103627	415	3	16	6126	1	3	f
103678	415	4	17	6127	0	3	f
103629	415	3	18	6126	0	2	t
103995	415	10	34	6133	1	3	t
103680	415	4	19	6127	0	3	t
103679	415	4	18	6127	0	3	t
103746	415	5	35	6128	0	2	t
103647	415	3	36	6126	1	3	t
103648	415	3	37	6126	0	1	t
103747	415	5	36	6128	2	3	t
103699	415	4	38	6127	0	3	f
103698	415	4	37	6127	0	3	f
103748	415	5	37	6128	0	3	f
103630	415	3	19	6126	2	3	t
103631	415	3	20	6126	0	3	f
103632	415	3	21	6126	0	1	t
103731	415	5	20	6128	0	3	f
103681	415	4	20	6127	0	3	f
103732	415	5	21	6128	0	3	t
103683	415	4	22	6127	0	3	t
103700	415	4	39	6127	0	1	t
103749	415	5	38	6128	0	3	f
103649	415	3	38	6126	1	3	t
103751	415	5	40	6128	0	3	f
103750	415	5	39	6128	0	3	t
103701	415	4	40	6127	1	3	t
103651	415	3	40	6126	2	3	t
103702	415	4	41	6127	0	3	t
103752	415	5	41	6128	0	3	t
103733	415	5	22	6128	0	3	f
103684	415	4	23	6127	0	3	f
103663	415	4	2	6127	0	3	t
103762	415	6	1	6129	1	3	t
103664	415	4	3	6127	0	3	t
103713	415	5	2	6128	0	3	f
103714	415	5	3	6128	0	3	f
103715	415	5	4	6128	0	1	t
103666	415	4	5	6127	0	3	t
103665	415	4	4	6127	0	3	t
103734	415	5	23	6128	0	3	f
103716	415	5	5	6128	1	3	t
103617	415	3	6	6126	0	1	f
103717	415	5	6	6128	0	2	t
103618	415	3	7	6126	0	2	t
103719	415	5	8	6128	0	3	t
103718	415	5	7	6128	2	3	t
103735	415	5	24	6128	0	2	t
103669	415	4	8	6127	0	3	t
103720	415	5	9	6128	0	3	t
103670	415	4	9	6127	0	3	f
103671	415	4	10	6127	0	3	t
103721	415	5	10	6128	0	3	f
103723	415	5	12	6128	0	3	t
103722	415	5	11	6128	0	3	t
103672	415	4	11	6127	0	3	t
103673	415	4	12	6127	0	3	t
103685	415	4	24	6127	0	3	t
103674	415	4	13	6127	0	3	t
103724	415	5	13	6128	0	3	f
103635	415	3	24	6126	1	3	t
103686	415	4	25	6127	0	3	t
103737	415	5	26	6128	0	3	t
103736	415	5	25	6128	2	3	t
103653	415	3	42	6126	0	2	t
103739	415	5	28	6128	0	3	t
103687	415	4	26	6127	0	3	f
103688	415	4	27	6127	0	3	t
103738	415	5	27	6128	0	3	t
103689	415	4	28	6127	0	3	t
103740	415	5	29	6128	0	3	f
103641	415	3	30	6126	0	1	t
103655	415	3	44	6126	0	1	t
103753	415	5	42	6128	0	3	t
103741	415	5	30	6128	0	1	t
103754	415	5	43	6128	0	3	t
103654	415	3	43	6126	2	3	t
103755	415	5	44	6128	0	3	t
103756	415	5	45	6128	0	3	f
103707	415	4	46	6127	0	1	t
103656	415	3	45	6126	1	3	f
103607	415	2	46	6125	0	1	t
103757	415	5	46	6128	0	3	f
103608	415	2	47	6125	1	3	t
103708	415	4	47	6127	1	3	t
103775	415	6	14	6129	0	2	f
103876	415	8	15	6131	0	1	t
103875	415	8	14	6131	1	3	t
103792	415	6	31	6129	0	1	t
103776	415	6	15	6129	0	1	t
104093	415	12	32	6135	2	0	t
103842	415	7	31	6130	0	1	t
103793	415	6	32	6129	1	3	t
103894	415	8	33	6131	0	1	t
103843	415	7	32	6130	1	3	t
103809	415	6	48	6129	2	0	t
103810	415	6	49	6129	0	1	t
103994	415	10	33	6133	3	0	t
103859	415	7	48	6130	1	3	t
105549	416	1	38	6164	0	2	t
103910	415	8	49	6131	0	3	t
103860	415	7	49	6130	0	3	f
107419	417	9	8	6202	0	3	f
105551	416	1	40	6164	0	2	t
105552	416	1	41	6164	0	2	f
103877	415	8	16	6131	1	3	t
103895	415	8	34	6131	1	3	t
103777	415	6	16	6129	1	3	f
103878	415	8	17	6131	0	2	t
103828	415	7	17	6130	0	3	f
103829	415	7	18	6130	0	1	t
103896	415	8	35	6131	0	3	t
103779	415	6	18	6129	1	2	t
103879	415	8	18	6131	2	3	t
103897	415	8	36	6131	0	1	t
103846	415	7	35	6130	0	3	t
103796	415	6	35	6129	1	3	t
103848	415	7	37	6130	0	1	t
103847	415	7	36	6130	0	3	f
103850	415	7	39	6130	0	3	t
103898	415	8	37	6131	1	3	t
103798	415	6	37	6129	2	3	t
103899	415	8	38	6131	0	3	f
103830	415	7	19	6130	1	3	f
103780	415	6	19	6129	2	3	t
103781	415	6	20	6129	0	1	t
103881	415	8	20	6131	0	1	t
103782	415	6	21	6129	1	3	t
103783	415	6	22	6129	0	2	f
103882	415	8	21	6131	1	3	f
103849	415	7	38	6130	1	3	t
103900	415	8	39	6131	0	3	t
103901	415	8	40	6131	0	1	f
103902	415	8	41	6131	0	3	t
103851	415	7	40	6130	0	3	f
103853	415	7	42	6130	0	1	t
103852	415	7	41	6130	0	3	f
103802	415	6	41	6129	2	1	t
103784	415	6	23	6129	0	1	t
103833	415	7	22	6130	0	3	f
103883	415	8	22	6131	1	3	t
103835	415	7	24	6130	0	3	t
103834	415	7	23	6130	0	3	f
103903	415	8	42	6131	0	3	f
103763	415	6	2	6129	0	1	t
103812	415	7	1	6130	1	3	t
103913	415	9	2	6132	0	3	t
103785	415	6	24	6129	1	3	t
103764	415	6	3	6129	1	3	t
103765	415	6	4	6129	0	1	t
103866	415	8	5	6131	0	3	t
103865	415	8	4	6131	0	3	t
103915	415	9	4	6132	0	3	t
103766	415	6	5	6129	1	3	t
103767	415	6	6	6129	0	1	t
103868	415	8	7	6131	0	3	t
103867	415	8	6	6131	0	3	f
103917	415	9	6	6132	0	3	f
103819	415	7	8	6130	0	1	t
103768	415	6	7	6129	1	2	t
103869	415	8	8	6131	0	3	f
103769	415	6	8	6129	2	3	t
103770	415	6	9	6129	0	1	t
103871	415	8	10	6131	0	3	f
103870	415	8	9	6131	0	3	f
103820	415	7	9	6130	1	3	f
103771	415	6	10	6129	1	3	t
103772	415	6	11	6129	0	2	t
103872	415	8	11	6131	0	2	t
103773	415	6	12	6129	2	3	t
103874	415	8	13	6131	0	1	t
103873	415	8	12	6131	2	3	t
103786	415	6	25	6129	0	1	t
103774	415	6	13	6129	0	1	f
103836	415	7	25	6130	0	3	t
103837	415	7	26	6130	0	1	t
103787	415	6	26	6129	1	3	t
103788	415	6	27	6129	0	1	t
103904	415	8	43	6131	0	3	t
103888	415	8	27	6131	0	2	t
103789	415	6	28	6129	1	3	t
103790	415	6	29	6129	0	1	t
103889	415	8	28	6131	2	3	t
103890	415	8	29	6131	0	2	t
103791	415	6	30	6129	1	3	t
103854	415	7	43	6130	1	3	t
103891	415	8	30	6131	2	3	t
103905	415	8	44	6131	0	2	t
103855	415	7	44	6130	0	3	t
103806	415	6	45	6129	0	1	t
103856	415	7	45	6130	0	3	t
103857	415	7	46	6130	0	3	f
103807	415	6	46	6129	1	3	t
103858	415	7	47	6130	0	1	t
103808	415	6	47	6129	0	2	t
104025	415	11	14	6134	2	0	t
104026	415	11	15	6134	1	0	t
103925	415	9	14	6132	0	3	f
104042	415	11	31	6134	1	0	t
103942	415	9	31	6132	0	3	t
103893	415	8	32	6131	0	3	f
103943	415	9	32	6132	0	3	f
104043	415	11	32	6134	1	2	t
103944	415	9	33	6132	0	3	t
104059	415	11	48	6134	1	0	f
104009	415	10	48	6133	1	0	f
104060	415	11	49	6134	1	0	t
104010	415	10	49	6133	1	0	f
103960	415	9	49	6132	0	3	f
107119	417	3	8	6196	0	3	f
105555	416	1	44	6164	0	2	t
105557	416	1	46	6164	0	2	f
105558	416	1	47	6164	0	2	f
103975	415	10	14	6133	1	2	t
103927	415	9	16	6132	1	0	f
103926	415	9	15	6132	0	1	t
103976	415	10	15	6133	2	0	f
104028	415	11	17	6134	2	0	t
104027	415	11	16	6134	1	2	t
104045	415	11	34	6134	1	0	t
103845	415	7	34	6130	0	3	t
103997	415	10	36	6133	1	0	t
104046	415	11	35	6134	1	2	t
103998	415	10	37	6133	1	0	t
103947	415	9	36	6132	0	1	t
104047	415	11	36	6134	2	0	t
104048	415	11	37	6134	1	0	f
103999	415	10	38	6133	1	0	t
103948	415	9	37	6132	1	3	t
103928	415	9	17	6132	1	3	f
103930	415	9	19	6132	0	3	t
103978	415	10	17	6133	1	3	f
104029	415	11	18	6134	1	0	t
103929	415	9	18	6132	1	3	t
103981	415	10	20	6133	2	0	t
103980	415	10	19	6133	1	2	t
103949	415	9	38	6132	0	3	f
104049	415	11	38	6134	1	2	f
104000	415	10	39	6133	1	0	f
104001	415	10	40	6133	1	0	t
103950	415	9	39	6132	0	3	t
104051	415	11	40	6134	1	0	t
103951	415	9	40	6132	0	3	f
104052	415	11	41	6134	1	2	t
104032	415	11	21	6134	1	0	t
103931	415	9	20	6132	0	3	t
103982	415	10	21	6133	1	0	f
103983	415	10	22	6133	1	0	f
103932	415	9	21	6132	0	3	t
104033	415	11	22	6134	1	2	f
104034	415	11	23	6134	1	0	t
104002	415	10	41	6133	1	3	t
103984	415	10	23	6133	1	0	t
103962	415	10	1	6133	2	0	t
104013	415	11	2	6134	1	0	t
104014	415	11	3	6134	1	0	t
104063	415	12	2	6135	1	3	f
104065	415	12	4	6135	1	0	t
103967	415	10	6	6133	1	0	t
104015	415	11	4	6134	1	0	f
104016	415	11	5	6134	1	0	f
104066	415	12	5	6135	1	2	f
103985	415	10	24	6133	1	2	t
104018	415	11	7	6134	2	0	t
104017	415	11	6	6134	1	2	t
103968	415	10	7	6133	1	2	f
103969	415	10	8	6133	1	0	t
103970	415	10	9	6133	1	0	t
104019	415	11	8	6134	1	0	t
104071	415	12	10	6135	1	0	f
104020	415	11	9	6134	1	2	t
104035	415	11	24	6134	1	2	t
103972	415	10	11	6133	1	0	t
103971	415	10	10	6133	1	0	f
104021	415	11	10	6134	2	0	f
103986	415	10	25	6133	2	0	t
104072	415	12	11	6135	1	2	t
104023	415	11	12	6134	1	0	t
104073	415	12	12	6135	2	0	t
103923	415	9	12	6132	0	3	t
104074	415	12	13	6135	1	2	t
104024	415	11	13	6134	1	2	t
104036	415	11	25	6134	2	0	t
104037	415	11	26	6134	1	0	f
103936	415	9	25	6132	0	3	f
103988	415	10	27	6133	2	0	t
104053	415	11	42	6134	2	0	t
103987	415	10	26	6133	1	2	t
103989	415	10	28	6133	1	0	f
103938	415	9	27	6132	0	3	t
103990	415	10	29	6133	1	0	t
104041	415	11	30	6134	1	0	t
104040	415	11	29	6134	2	0	t
104003	415	10	42	6133	3	0	t
104054	415	11	43	6134	1	0	t
103941	415	9	30	6132	0	3	t
104004	415	10	43	6133	1	0	f
104005	415	10	44	6133	1	0	t
104006	415	10	45	6133	1	0	t
104055	415	11	44	6134	1	0	f
103957	415	9	46	6132	0	3	t
104056	415	11	45	6134	1	0	f
104007	415	10	46	6133	1	2	t
104008	415	10	47	6133	2	0	t
103958	415	9	47	6132	0	3	t
104192	415	14	31	6137	2	0	t
104142	415	13	31	6136	3	0	t
104193	415	14	32	6137	1	0	f
104159	415	13	48	6136	1	0	f
104194	415	14	33	6137	1	0	t
104143	415	13	32	6136	1	3	t
104110	415	12	49	6135	1	0	f
103795	415	6	34	6129	0	1	t
103794	415	6	33	6129	0	3	f
104109	415	12	48	6135	1	0	f
104160	415	13	49	6136	1	0	f
104210	415	14	49	6137	2	0	f
105988	416	10	27	6173	1	0	f
105738	416	5	27	6168	0	2	t
105563	416	2	2	6165	0	1	t
104195	415	14	34	6137	1	0	f
104125	415	13	14	6136	1	0	f
104075	415	12	14	6135	2	0	t
104196	415	14	35	6137	1	0	f
104176	415	14	15	6137	1	0	t
104227	415	15	16	6138	1	0	t
104126	415	13	15	6136	1	2	t
104096	415	12	35	6135	2	3	t
104097	415	12	36	6135	3	0	t
104147	415	13	36	6136	1	3	t
104197	415	14	36	6137	1	3	f
104148	415	13	37	6136	3	0	t
104199	415	14	38	6137	1	0	t
104098	415	12	37	6135	1	2	t
104099	415	12	38	6135	2	0	f
104076	415	12	15	6135	1	2	t
104200	415	14	39	6137	1	0	f
104177	415	14	16	6137	1	0	f
104178	415	14	17	6137	1	0	t
104077	415	12	16	6135	2	0	t
104179	415	14	18	6137	1	0	f
104228	415	15	17	6138	1	0	t
104149	415	13	38	6136	1	3	t
104100	415	12	39	6135	2	0	t
104201	415	14	40	6137	1	2	t
104202	415	14	41	6137	2	0	f
104151	415	13	40	6136	1	3	t
104152	415	13	41	6136	3	0	t
104203	415	14	42	6137	2	1	t
104103	415	12	42	6135	1	3	f
104078	415	12	17	6135	1	2	t
104129	415	13	18	6136	2	0	t
104079	415	12	18	6135	2	0	f
104180	415	14	19	6137	1	0	t
104181	415	14	20	6137	1	0	t
104130	415	13	19	6136	1	0	f
104080	415	12	19	6135	2	3	t
104153	415	13	42	6136	1	3	f
104104	415	12	43	6135	1	3	f
104105	415	12	44	6135	1	0	t
104204	415	14	43	6137	1	3	f
104081	415	12	20	6135	3	0	t
104182	415	14	21	6137	1	0	f
104162	415	14	1	6137	1	2	t
104113	415	13	2	6136	1	0	t
104213	415	15	2	6138	2	0	f
104131	415	13	20	6136	1	3	t
104114	415	13	3	6136	1	2	t
104215	415	15	4	6138	1	0	f
104115	415	13	4	6136	2	0	t
104116	415	13	5	6136	1	0	t
104117	415	13	6	6136	1	0	t
104216	415	15	5	6138	1	3	t
104118	415	13	7	6136	1	0	t
104217	415	15	6	6138	3	0	t
104218	415	15	7	6138	1	0	t
104119	415	13	8	6136	1	0	t
104120	415	13	9	6136	1	0	t
104169	415	14	8	6137	3	0	t
104121	415	13	10	6136	1	0	t
104170	415	14	9	6137	1	3	t
104221	415	15	10	6138	2	0	f
104122	415	13	11	6136	1	0	t
104222	415	15	11	6138	2	1	t
104082	415	12	21	6135	1	0	f
104123	415	13	12	6136	1	0	t
104124	415	13	13	6136	1	0	t
104223	415	15	12	6138	1	0	f
104132	415	13	21	6136	3	0	t
104083	415	12	22	6135	1	2	f
104184	415	14	23	6137	1	0	t
104183	415	14	22	6137	1	3	f
104084	415	12	23	6135	1	2	t
104185	415	14	24	6137	1	0	t
104206	415	14	45	6137	1	0	f
104085	415	12	24	6135	2	0	t
104186	415	14	25	6137	1	0	t
104187	415	14	26	6137	1	0	t
104086	415	12	25	6135	1	2	t
104205	415	14	44	6137	1	0	t
104087	415	12	26	6135	2	0	f
104138	415	13	27	6136	1	0	t
104188	415	14	27	6137	1	0	t
104139	415	13	28	6136	1	0	f
104189	415	14	28	6137	1	0	f
104140	415	13	29	6136	1	0	f
104190	415	14	29	6137	1	2	t
104191	415	14	30	6137	2	1	f
104141	415	13	30	6136	1	3	t
104107	415	12	46	6135	2	0	t
104106	415	12	45	6135	1	2	t
104207	415	14	46	6137	1	3	t
104108	415	12	47	6135	1	2	f
104208	415	14	47	6137	3	1	t
104292	415	16	31	6139	1	0	t
104293	415	16	32	6139	1	0	f
104242	415	15	31	6138	1	0	t
104259	415	15	48	6138	1	0	t
104243	415	15	32	6138	1	0	f
104294	415	16	33	6139	1	0	f
104309	415	16	48	6139	1	0	f
104260	415	15	49	6138	1	0	t
106388	416	18	27	6181	2	0	t
104360	415	17	49	6140	1	0	f
104310	415	16	49	6139	1	0	f
105567	416	2	6	6165	0	1	t
105569	416	2	8	6165	0	1	t
104325	415	17	14	6140	1	0	t
104275	415	16	14	6139	1	0	f
104276	415	16	15	6139	1	0	t
104375	415	18	14	6141	3	0	t
104326	415	17	15	6140	1	0	t
104327	415	17	16	6140	1	0	f
104094	415	12	33	6135	1	2	t
104944	415	29	33	6152	2	1	t
104095	415	12	34	6135	2	0	f
104295	415	16	34	6139	1	2	t
104296	415	16	35	6139	2	0	t
105570	416	2	9	6165	1	2	t
104297	415	16	36	6139	1	0	t
104346	415	17	35	6140	3	0	t
104347	415	17	36	6140	1	0	t
104298	415	16	37	6139	1	0	t
104299	415	16	38	6139	1	0	t
104377	415	18	16	6141	1	0	f
104378	415	18	17	6141	1	0	t
104379	415	18	18	6141	1	0	t
104328	415	17	17	6140	1	3	t
104279	415	16	18	6139	2	0	t
104380	415	18	19	6141	1	0	t
104329	415	17	18	6140	3	0	f
104248	415	15	37	6138	1	0	f
104348	415	17	37	6140	1	0	f
104249	415	15	38	6138	1	2	t
104300	415	16	39	6139	1	0	f
104251	415	15	40	6138	2	0	t
104250	415	15	39	6138	2	0	f
104252	415	15	41	6138	1	0	t
104301	415	16	40	6139	1	2	t
104280	415	16	19	6139	1	0	f
104231	415	15	20	6138	1	0	t
104381	415	18	20	6141	1	0	f
104382	415	18	21	6141	1	0	t
104383	415	18	22	6141	1	0	t
104332	415	17	21	6140	1	0	f
104253	415	15	42	6138	1	0	t
104352	415	17	41	6140	2	0	f
104302	415	16	41	6139	2	0	f
104353	415	17	42	6140	2	0	f
104304	415	16	43	6139	1	0	t
104305	415	16	44	6139	1	0	t
104254	415	15	43	6138	1	0	f
104232	415	15	21	6138	1	3	f
104384	415	18	23	6141	1	0	t
104263	415	16	2	6139	1	0	t
104262	415	16	1	6139	2	0	t
104315	415	17	4	6140	1	0	f
104363	415	18	2	6141	1	0	t
104264	415	16	3	6139	1	0	f
104333	415	17	22	6140	1	2	t
104265	415	16	4	6139	1	0	f
104266	415	16	5	6139	1	2	f
104267	415	16	6	6139	1	0	t
104316	415	17	5	6140	1	2	f
104367	415	18	6	6141	2	1	t
104368	415	18	7	6141	1	0	f
104269	415	16	8	6139	1	0	f
104268	415	16	7	6139	1	2	f
104283	415	16	22	6139	1	2	t
104320	415	17	9	6140	2	0	f
104319	415	17	8	6140	1	2	t
104270	415	16	9	6139	1	3	f
104271	415	16	10	6139	1	0	t
104371	415	18	10	6141	1	0	t
104272	415	16	11	6139	1	2	f
104372	415	18	11	6141	1	3	t
104373	415	18	12	6141	3	0	t
104234	415	15	23	6138	1	0	t
104273	415	16	12	6139	1	2	t
104385	415	18	24	6141	1	0	t
104374	415	18	13	6141	1	3	t
104334	415	17	23	6140	2	0	t
104335	415	17	24	6140	1	0	f
104236	415	15	25	6138	1	0	t
104235	415	15	24	6138	1	0	f
104287	415	16	26	6139	1	0	t
104386	415	18	25	6141	1	0	f
104336	415	17	25	6140	1	3	t
104338	415	17	27	6140	1	0	t
104237	415	15	26	6138	1	2	t
104288	415	16	27	6139	1	0	f
104339	415	17	28	6140	1	0	t
104240	415	15	29	6138	1	0	t
104289	415	16	28	6139	1	2	t
104340	415	17	29	6140	1	0	f
104241	415	15	30	6138	1	0	t
104341	415	17	30	6140	1	2	t
104255	415	15	44	6138	1	2	t
104306	415	16	45	6139	1	0	t
104307	415	16	46	6139	1	0	t
104356	415	17	45	6140	1	0	f
104258	415	15	47	6138	1	0	t
104357	415	17	46	6140	1	0	t
104308	415	16	47	6139	1	0	t
104392	415	18	31	6141	1	0	t
104492	415	20	31	6143	0	1	t
104409	415	18	48	6141	1	0	t
104542	415	21	31	6144	2	1	t
104459	415	19	48	6142	1	0	f
104410	415	18	49	6141	1	0	f
105538	416	1	27	6164	0	2	t
103510	415	0	49	6123	0	2	t
104510	415	20	49	6143	2	0	t
105573	416	2	12	6165	0	1	t
104425	415	19	14	6142	1	2	t
104525	415	21	14	6144	2	1	t
104526	415	21	15	6144	2	0	t
104475	415	20	14	6143	2	1	f
104527	415	21	16	6144	0	1	t
104426	415	19	15	6142	2	0	t
104393	415	18	32	6141	1	0	f
104394	415	18	33	6141	1	0	t
104493	415	20	32	6143	2	0	f
103693	415	4	32	6127	0	3	f
104395	415	18	34	6141	1	0	t
104494	415	20	33	6143	2	1	f
104495	415	20	34	6143	2	0	t
104496	415	20	35	6143	0	1	t
104445	415	19	34	6142	1	3	t
104397	415	18	36	6141	1	0	t
104396	415	18	35	6141	1	0	t
105575	416	2	14	6165	0	2	f
105576	416	2	15	6165	0	2	f
104478	415	20	17	6143	0	1	t
104477	415	20	16	6143	2	0	t
104479	415	20	18	6143	2	0	t
104528	415	21	17	6144	2	3	t
104429	415	19	18	6142	1	2	f
104480	415	20	19	6143	0	1	t
104529	415	21	18	6144	3	1	t
104447	415	19	36	6142	3	0	t
104398	415	18	37	6141	1	0	f
104497	415	20	36	6143	2	1	f
104448	415	19	37	6142	1	2	t
104399	415	18	38	6141	1	0	t
104499	415	20	38	6143	0	1	t
104400	415	18	39	6141	1	0	t
104481	415	20	20	6143	2	0	t
104430	415	19	19	6142	1	3	f
104500	415	20	39	6143	2	0	t
104431	415	19	20	6142	1	2	t
104482	415	20	21	6143	0	1	t
104432	415	19	21	6142	2	0	t
104533	415	21	22	6144	2	1	t
104501	415	20	40	6143	0	1	t
104402	415	18	41	6141	1	0	t
104401	415	18	40	6141	1	0	t
104451	415	19	40	6142	2	0	t
104403	415	18	42	6141	1	0	t
104502	415	20	41	6143	2	0	f
104404	415	18	43	6141	1	0	t
104503	415	20	42	6143	2	0	f
104505	415	20	44	6143	0	1	t
104433	415	19	22	6142	1	3	t
104434	415	19	23	6142	3	0	t
104462	415	20	1	6143	2	1	t
104513	415	21	2	6144	2	0	t
104483	415	20	22	6143	2	3	t
104514	415	21	3	6144	0	1	t
104413	415	19	2	6142	2	0	t
104415	415	19	4	6142	3	0	t
104515	415	21	4	6144	2	1	t
104416	415	19	5	6142	1	3	f
104417	415	19	6	6142	1	2	t
104516	415	21	5	6144	2	3	f
104504	415	20	43	6143	2	0	t
104418	415	19	7	6142	2	0	t
104467	415	20	6	6143	2	1	t
104469	415	20	8	6143	2	1	f
104468	415	20	7	6143	2	1	t
104534	415	21	23	6144	2	1	t
104519	415	21	8	6144	2	1	f
104470	415	20	9	6143	2	0	f
104520	415	21	9	6144	2	1	t
104421	415	19	10	6142	2	0	f
104535	415	21	24	6144	2	0	t
104521	415	21	10	6144	2	1	t
104422	415	19	11	6142	2	0	t
104522	415	21	11	6144	2	1	t
104523	415	21	12	6144	2	0	t
104524	415	21	13	6144	0	1	t
104473	415	20	12	6143	3	0	t
104536	415	21	25	6144	0	1	t
104435	415	19	24	6142	1	2	f
104387	415	18	26	6141	1	0	t
104436	415	19	25	6142	1	2	f
104487	415	20	26	6143	0	1	t
104389	415	18	28	6141	1	0	f
104537	415	21	26	6144	2	0	t
104388	415	18	27	6141	1	0	f
104488	415	20	27	6143	2	1	f
104489	415	20	28	6143	2	0	t
104490	415	20	29	6143	0	1	t
104390	415	18	29	6141	1	0	t
104391	415	18	30	6141	1	0	t
104491	415	20	30	6143	2	0	t
104541	415	21	30	6144	2	1	t
104405	415	18	44	6141	1	0	t
104406	415	18	45	6141	1	0	f
104407	415	18	46	6141	1	0	t
104506	415	20	45	6143	2	1	f
104408	415	18	47	6141	1	0	t
104507	415	20	46	6143	2	3	t
104458	415	19	47	6142	2	0	t
104659	415	23	48	6146	0	2	t
105260	415	35	49	6158	3	0	t
104559	415	21	48	6144	2	1	f
104660	415	23	49	6146	2	1	t
104560	415	21	49	6144	2	1	f
104610	415	22	49	6145	2	1	f
105888	416	8	27	6171	0	2	t
108019	417	21	8	6214	2	1	f
105689	416	4	28	6167	0	1	t
104625	415	23	14	6146	2	1	t
104575	415	22	14	6145	2	1	f
104675	415	24	14	6147	2	1	f
104626	415	23	15	6146	2	0	f
104577	415	22	16	6145	2	1	t
104576	415	22	15	6145	2	1	t
104692	415	24	31	6147	2	1	t
104642	415	23	31	6146	2	3	f
104643	415	23	32	6146	2	1	t
104693	415	24	32	6147	2	1	t
104044	415	11	33	6134	2	0	t
104545	415	21	34	6144	0	1	t
103694	415	4	33	6127	0	3	f
104644	415	23	33	6146	2	3	t
104627	415	23	16	6146	2	1	t
104578	415	22	17	6145	2	1	t
104579	415	22	18	6145	2	1	t
104628	415	23	17	6146	2	3	t
104679	415	24	18	6147	3	1	f
104696	415	24	35	6147	2	1	t
104629	415	23	18	6146	3	1	f
104595	415	22	34	6145	2	1	t
104695	415	24	34	6147	2	1	t
104597	415	22	36	6145	2	1	t
104596	415	22	35	6145	2	1	f
104546	415	21	35	6144	2	3	t
104697	415	24	36	6147	2	1	f
104598	415	22	37	6145	2	1	t
104647	415	23	36	6146	2	1	f
104580	415	22	19	6145	2	1	t
104680	415	24	19	6147	3	2	t
104631	415	23	20	6146	0	2	t
104581	415	22	20	6145	2	1	f
104632	415	23	21	6146	2	1	f
104582	415	22	21	6145	2	1	f
104683	415	24	22	6147	2	0	t
104549	415	21	38	6144	2	1	t
104698	415	24	37	6147	2	3	t
104648	415	23	37	6146	2	3	t
104600	415	22	39	6145	2	1	t
104599	415	22	38	6145	2	1	t
104649	415	23	38	6146	3	1	t
104601	415	22	40	6145	2	1	t
104550	415	21	39	6144	2	1	f
104650	415	23	39	6146	2	1	f
104551	415	21	40	6144	2	1	t
104684	415	24	23	6147	0	1	t
104583	415	22	22	6145	2	1	t
104662	415	24	1	6147	0	1	t
104633	415	23	22	6146	2	3	t
104613	415	23	2	6146	2	1	t
104565	415	22	4	6145	2	0	t
104663	415	24	2	6147	2	1	f
104614	415	23	3	6146	2	3	f
104665	415	24	4	6147	0	3	t
104566	415	22	5	6145	0	2	t
104617	415	23	6	6146	2	1	t
104666	415	24	5	6147	3	1	t
104685	415	24	24	6147	2	1	t
104567	415	22	6	6145	2	1	t
104669	415	24	8	6147	0	1	t
104618	415	23	7	6146	2	1	t
104568	415	22	7	6145	2	3	f
104584	415	22	23	6145	2	1	t
104569	415	22	8	6145	2	1	t
104570	415	22	9	6145	2	0	t
104670	415	24	9	6147	2	1	t
104621	415	23	10	6146	2	0	t
104622	415	23	11	6146	0	1	t
104571	415	22	10	6145	0	2	t
104673	415	24	12	6147	2	1	t
104572	415	22	11	6145	2	1	t
104674	415	24	13	6147	2	1	t
104573	415	22	12	6145	2	1	t
104552	415	21	41	6144	2	1	f
104637	415	23	26	6146	0	1	t
104585	415	22	24	6145	2	1	t
104686	415	24	25	6147	2	1	t
104586	415	22	25	6145	2	1	t
104638	415	23	27	6146	2	0	t
104687	415	24	26	6147	2	1	t
104639	415	23	28	6146	0	3	t
104688	415	24	27	6147	2	1	t
104640	415	23	29	6146	3	0	t
104689	415	24	28	6147	2	1	t
104690	415	24	29	6147	2	1	t
104641	415	23	30	6146	0	1	t
104602	415	22	41	6145	2	1	f
104691	415	24	30	6147	2	1	t
104603	415	22	42	6145	2	1	f
104553	415	21	42	6144	2	1	f
104654	415	23	43	6146	0	1	t
104604	415	22	43	6145	2	1	f
104655	415	23	44	6146	2	0	t
104556	415	21	45	6144	2	0	t
104605	415	22	44	6145	2	1	f
104656	415	23	45	6146	0	2	f
104657	415	23	46	6146	0	1	t
104557	415	21	46	6144	0	1	f
104558	415	21	47	6144	0	1	t
104658	415	23	47	6146	2	0	t
104709	415	24	48	6147	2	1	t
104809	415	26	48	6149	2	1	f
108992	417	40	31	6233	1	2	t
104810	415	26	49	6149	2	1	f
104710	415	24	49	6147	2	1	f
105010	415	30	49	6153	3	1	t
104460	415	19	49	6142	1	3	t
106188	416	14	27	6177	1	2	t
104725	415	25	14	6148	3	0	t
104726	415	25	15	6148	0	1	f
104775	415	26	14	6149	2	1	t
104825	415	27	14	6150	3	1	t
104727	415	25	16	6148	0	3	f
104776	415	26	15	6149	2	1	t
104742	415	25	31	6148	2	3	t
104792	415	26	31	6149	2	3	f
104843	415	27	32	6150	2	0	f
106639	416	23	28	6186	2	1	t
104444	415	19	33	6142	2	0	t
104443	415	19	32	6142	1	2	t
104694	415	24	33	6147	2	1	t
104844	415	27	33	6150	2	3	t
104795	415	26	34	6149	2	0	f
104728	415	25	17	6148	0	3	f
104777	415	26	16	6149	2	1	t
104778	415	26	17	6149	2	1	t
104729	415	25	18	6148	0	1	t
104830	415	27	19	6150	0	1	t
104829	415	27	18	6150	2	0	t
104779	415	26	18	6149	2	1	t
104845	415	27	34	6150	3	1	t
104846	415	27	35	6150	2	0	t
104796	415	26	35	6149	2	1	f
104847	415	27	36	6150	0	1	t
104797	415	26	36	6149	2	3	f
104798	415	26	37	6149	2	1	t
104799	415	26	38	6149	2	1	t
104848	415	27	37	6150	2	3	t
104781	415	26	20	6149	2	1	t
104730	415	25	19	6148	2	3	t
104731	415	25	20	6148	3	1	t
104833	415	27	22	6150	0	1	t
104782	415	26	21	6149	2	1	f
104732	415	25	21	6148	2	3	t
104849	415	27	38	6150	3	1	t
104700	415	24	39	6147	3	0	t
104699	415	24	38	6147	3	1	f
104800	415	26	39	6149	2	1	f
104701	415	24	40	6147	0	1	t
104850	415	27	39	6150	2	3	t
104801	415	26	40	6149	2	1	t
104852	415	27	41	6150	2	1	f
104751	415	25	40	6148	2	3	t
104703	415	24	42	6147	2	0	f
104834	415	27	23	6150	2	0	f
104783	415	26	22	6149	2	1	t
104762	415	26	1	6149	0	1	t
104813	415	27	2	6150	0	1	f
104733	415	25	22	6148	3	1	t
104814	415	27	3	6150	0	2	f
104713	415	25	2	6148	2	3	t
104815	415	27	4	6150	0	2	t
104765	415	26	4	6149	3	1	f
104766	415	26	5	6149	3	1	t
104717	415	25	6	6148	0	1	t
104816	415	27	5	6150	2	3	t
104767	415	26	6	6149	2	0	t
104768	415	26	7	6149	0	1	t
104784	415	26	23	6149	2	1	t
104718	415	25	7	6148	2	3	t
104769	415	26	8	6149	2	0	t
104719	415	25	8	6148	3	1	t
104770	415	26	9	6149	0	1	f
104821	415	27	10	6150	0	1	t
104720	415	25	9	6148	2	3	t
104823	415	27	12	6150	2	0	t
104771	415	26	10	6149	0	1	t
104772	415	26	11	6149	2	3	t
104785	415	26	24	6149	2	1	t
104822	415	27	11	6150	2	3	f
104824	415	27	13	6150	0	3	t
104773	415	26	12	6149	3	1	t
104702	415	24	41	6147	2	1	f
104735	415	25	24	6148	3	1	t
104786	415	26	25	6149	2	1	t
104736	415	25	25	6148	2	3	t
104837	415	27	26	6150	0	1	t
104838	415	27	27	6150	2	0	t
104787	415	26	26	6149	2	1	f
104839	415	27	28	6150	0	3	f
104788	415	26	27	6149	2	1	f
104802	415	26	41	6149	2	1	f
104840	415	27	29	6150	0	1	t
104739	415	25	28	6148	3	1	t
104791	415	26	30	6149	2	1	f
104740	415	25	29	6148	2	3	t
104741	415	25	30	6148	3	1	t
104804	415	26	43	6149	3	0	t
104803	415	26	42	6149	2	3	t
104853	415	27	42	6150	2	3	t
104854	415	27	43	6150	3	1	t
104805	415	26	44	6149	0	1	t
104704	415	24	43	6147	2	3	t
104706	415	24	45	6147	2	1	t
104755	415	25	44	6148	2	3	t
104707	415	24	46	6147	2	1	t
104806	415	26	45	6149	2	1	f
104807	415	26	46	6149	2	1	t
104808	415	26	47	6149	2	1	t
104708	415	24	47	6147	2	1	t
106838	416	27	27	6190	2	1	f
104859	415	27	48	6150	3	0	t
104909	415	28	48	6151	2	1	f
104860	415	27	49	6150	0	1	t
104593	415	22	32	6145	2	1	t
104925	415	29	14	6152	0	1	t
104875	415	28	14	6151	2	1	t
104876	415	28	15	6151	2	1	t
104926	415	29	15	6152	2	3	t
104977	415	30	16	6153	0	2	t
104892	415	28	31	6151	2	3	t
104928	415	29	17	6152	0	1	t
104959	415	29	48	6152	3	1	t
104942	415	29	31	6152	2	3	t
104910	415	28	49	6151	2	1	f
104793	415	26	32	6149	2	1	t
104960	415	29	49	6152	2	1	f
104594	415	22	33	6145	2	1	f
104945	415	29	34	6152	2	0	f
104794	415	26	33	6149	2	1	f
104895	415	28	34	6151	2	0	f
104896	415	28	35	6151	2	1	t
104760	415	25	49	6148	2	3	t
105578	416	2	17	6165	0	1	t
105580	416	2	19	6165	0	1	f
105582	416	2	21	6165	0	1	t
105583	416	2	22	6165	1	2	t
104927	415	29	16	6152	3	0	t
104979	415	30	18	6153	0	2	t
104978	415	30	17	6153	3	0	t
104930	415	29	19	6152	2	0	t
104929	415	29	18	6152	2	1	t
104879	415	28	18	6151	2	1	t
104995	415	30	34	6153	3	2	t
104946	415	29	35	6152	2	1	f
104897	415	28	36	6151	2	1	f
104997	415	30	36	6153	3	2	t
104898	415	28	37	6151	2	1	t
104899	415	28	38	6151	2	1	t
104998	415	30	37	6153	3	2	t
105001	415	30	40	6153	0	2	t
104949	415	29	38	6152	3	1	f
104931	415	29	20	6152	0	1	t
104980	415	30	19	6153	3	2	t
104881	415	28	20	6151	2	1	f
104882	415	28	21	6151	2	1	t
104983	415	30	22	6153	0	2	f
104932	415	29	21	6152	2	1	f
104984	415	30	23	6153	0	1	t
104999	415	30	38	6153	3	2	f
104950	415	29	39	6152	3	0	f
104900	415	28	39	6151	2	1	t
104901	415	28	40	6151	2	1	t
105002	415	30	41	6153	3	0	t
104902	415	28	41	6151	2	1	t
105003	415	30	42	6153	0	2	t
104903	415	28	42	6151	2	1	t
104883	415	28	22	6151	2	1	t
104863	415	28	2	6151	2	1	t
104912	415	29	1	6152	2	3	f
104933	415	29	22	6152	2	3	t
104864	415	28	3	6151	2	1	t
104913	415	29	2	6152	2	1	f
104965	415	30	4	6153	3	0	t
104966	415	30	5	6153	0	2	t
104865	415	28	4	6151	2	1	t
104866	415	28	5	6151	2	0	t
104917	415	29	6	6152	0	1	t
104867	415	28	6	6151	0	1	f
104868	415	28	7	6151	0	1	t
104884	415	28	23	6151	2	1	t
104919	415	29	8	6152	2	1	f
104918	415	29	7	6152	2	3	f
104869	415	28	8	6151	2	1	f
104870	415	28	9	6151	2	3	t
104871	415	28	10	6151	3	1	t
104920	415	29	9	6152	2	3	t
104921	415	29	10	6152	3	1	f
104922	415	29	11	6152	3	0	t
104935	415	29	24	6152	3	0	t
104872	415	28	11	6151	2	3	t
104923	415	29	12	6152	0	1	t
104924	415	29	13	6152	2	0	t
104873	415	28	12	6151	3	1	t
104936	415	29	25	6152	0	1	t
104874	415	28	13	6151	2	3	f
104985	415	30	24	6153	1	2	t
104953	415	29	42	6152	3	1	t
104986	415	30	25	6153	3	1	f
104937	415	29	26	6152	2	0	f
104887	415	28	26	6151	2	1	t
104888	415	28	27	6151	2	1	f
104938	415	29	27	6152	2	1	f
104989	415	30	28	6153	0	1	t
104939	415	29	28	6152	2	0	t
104940	415	29	29	6152	0	1	t
104990	415	30	29	6153	1	2	t
104941	415	29	30	6152	2	1	t
104904	415	28	43	6151	2	1	t
104891	415	28	30	6151	2	1	f
104955	415	29	44	6152	0	1	t
105004	415	30	43	6153	3	2	t
104905	415	28	44	6151	2	1	t
104855	415	27	44	6150	2	3	t
104956	415	29	45	6152	2	1	t
104857	415	27	46	6150	0	1	t
104906	415	28	45	6151	2	1	t
104957	415	29	46	6152	2	1	t
104858	415	27	47	6150	2	3	t
104958	415	29	47	6152	2	3	t
105125	415	33	14	6156	0	2	t
105076	415	32	15	6155	3	2	t
105075	415	32	14	6155	1	2	t
105142	415	33	31	6156	1	2	f
105126	415	33	15	6156	3	2	f
105077	415	32	16	6155	3	2	f
105078	415	32	17	6155	3	1	t
105127	415	33	16	6156	3	2	f
105143	415	33	32	6156	1	2	t
105092	415	32	31	6155	3	2	t
105159	415	33	48	6156	3	2	t
104743	415	25	32	6148	3	1	t
105060	415	31	49	6154	3	2	t
105093	415	32	32	6155	3	1	t
104744	415	25	33	6148	2	3	t
105144	415	33	33	6156	3	2	t
105095	415	32	34	6155	3	2	t
105109	415	32	48	6155	3	2	f
105110	415	32	49	6155	3	2	f
105160	415	33	49	6156	3	2	f
106590	416	22	29	6185	2	1	f
105463	416	0	2	6163	1	2	t
105465	416	0	4	6163	1	2	t
105128	415	33	17	6156	3	2	t
105129	415	33	18	6156	3	0	t
105028	415	31	17	6154	3	2	t
105130	415	33	19	6156	0	2	t
105079	415	32	18	6155	1	2	t
105145	415	33	34	6156	3	2	t
105030	415	31	19	6154	3	2	t
105096	415	32	35	6155	3	1	t
105146	415	33	35	6156	3	2	t
105097	415	32	36	6155	1	2	t
105098	415	32	37	6155	3	1	t
105147	415	33	36	6156	3	2	t
105047	415	31	36	6154	3	2	t
105148	415	33	37	6156	3	2	t
105099	415	32	38	6155	1	2	t
105466	416	0	5	6163	0	2	f
105031	415	31	20	6154	3	2	t
105131	415	33	20	6156	3	2	f
105132	415	33	21	6156	3	1	t
105133	415	33	22	6156	1	2	t
105032	415	31	21	6154	3	2	t
105082	415	32	21	6155	3	2	t
105084	415	32	23	6155	3	1	t
105033	415	31	22	6154	3	2	t
105149	415	33	38	6156	3	1	f
105150	415	33	39	6156	3	0	t
105151	415	33	40	6156	0	3	f
105100	415	32	39	6155	3	2	f
105152	415	33	41	6156	0	1	t
105101	415	32	40	6155	3	2	t
105051	415	31	40	6154	3	2	t
105153	415	33	42	6156	1	2	t
105102	415	32	41	6155	3	2	f
105054	415	31	43	6154	3	2	t
105134	415	33	23	6156	3	2	t
105085	415	32	24	6155	1	2	t
105161	415	34	0	6157	3	0	t
105113	415	33	2	6156	3	0	t
105135	415	33	24	6156	3	1	t
105013	415	31	2	6154	3	0	t
105114	415	33	3	6156	0	2	t
105015	415	31	4	6154	0	3	f
105014	415	31	3	6154	0	3	f
105136	415	33	25	6156	1	2	t
105065	415	32	4	6155	1	2	t
105016	415	31	5	6154	0	2	t
105165	415	34	4	6157	3	1	f
105067	415	32	6	6155	1	2	t
105066	415	32	5	6155	3	1	t
105118	415	33	7	6156	1	2	t
105117	415	33	6	6156	3	1	t
105017	415	31	6	6154	3	2	t
105068	415	32	7	6155	3	1	f
105069	415	32	8	6155	3	0	t
105018	415	31	7	6154	3	2	t
105070	415	32	9	6155	0	1	t
105119	415	33	8	6156	3	2	f
105120	415	33	9	6156	3	2	t
105071	415	32	10	6155	1	2	f
105122	415	33	11	6156	3	0	t
105121	415	33	10	6156	3	2	f
105072	415	32	11	6155	1	2	t
105123	415	33	12	6156	0	2	f
105073	415	32	12	6155	3	1	t
105124	415	33	13	6156	0	3	f
105087	415	32	26	6155	3	1	f
105086	415	32	25	6155	3	2	t
105074	415	32	13	6155	1	2	f
105036	415	31	25	6154	3	2	t
105138	415	33	27	6156	3	1	t
105137	415	33	26	6156	3	2	f
105053	415	31	42	6154	3	2	t
105139	415	33	28	6156	1	2	t
105088	415	32	27	6155	3	1	f
105090	415	32	29	6155	3	1	t
105140	415	33	29	6156	3	2	f
105091	415	32	30	6155	1	2	t
105141	415	33	30	6156	3	1	t
105154	415	33	43	6156	3	2	t
105155	415	33	44	6156	3	0	t
105156	415	33	45	6156	0	1	t
105105	415	32	44	6155	3	2	t
105157	415	33	46	6156	1	2	t
105106	415	32	45	6155	3	2	f
105107	415	32	46	6155	3	1	t
105108	415	32	47	6155	1	2	t
105158	415	33	47	6156	3	2	t
105175	415	34	14	6157	0	2	f
105176	415	34	15	6157	0	1	t
105225	415	35	14	6158	3	1	t
104975	415	30	14	6153	3	2	f
105192	415	34	31	6157	1	2	t
105243	415	35	32	6158	1	2	t
107269	417	6	8	6199	1	3	t
105209	415	34	48	6157	0	2	t
105310	415	36	49	6159	3	1	t
103993	415	10	32	6133	1	3	t
103844	415	7	33	6130	0	3	t
105094	415	32	33	6155	1	2	t
105244	415	35	33	6158	3	2	t
105195	415	34	34	6157	1	2	t
105296	415	36	35	6159	1	0	f
105309	415	36	48	6159	1	3	t
105210	415	34	49	6157	3	2	f
105468	416	0	7	6163	0	2	t
105470	416	0	9	6163	0	2	t
105472	416	0	11	6163	0	2	t
105226	415	35	15	6158	1	2	t
105227	415	35	16	6158	3	0	t
105177	415	34	16	6157	1	2	t
105228	415	35	17	6158	0	1	t
105245	415	35	34	6158	3	1	t
105178	415	34	17	6157	3	1	t
105179	415	34	18	6157	1	0	f
105196	415	34	35	6157	3	0	t
105197	415	34	36	6157	0	2	f
105246	415	35	35	6158	1	2	t
105297	415	36	36	6159	1	3	t
105198	415	34	37	6157	0	1	t
105248	415	35	37	6158	1	2	t
105199	415	34	38	6157	1	2	f
105200	415	34	39	6157	1	2	t
105473	416	0	12	6163	0	2	t
105229	415	35	18	6158	1	2	t
105230	415	35	19	6158	3	0	t
105180	415	34	19	6157	1	2	t
105231	415	35	20	6158	0	2	t
105182	415	34	21	6157	3	0	t
105181	415	34	20	6157	3	2	f
105232	415	35	21	6158	3	2	f
105183	415	34	22	6157	0	1	t
105249	415	35	38	6158	3	2	f
105251	415	35	40	6158	1	2	t
105250	415	35	39	6158	3	1	t
105300	415	36	39	6159	3	2	f
105302	415	36	41	6159	1	0	f
105201	415	34	40	6157	3	2	t
105252	415	35	41	6158	3	1	t
105303	415	36	42	6159	1	0	f
105283	415	36	22	6159	3	0	t
105284	415	36	23	6159	0	1	t
105233	415	35	22	6158	3	1	t
105184	415	34	23	6157	1	2	t
105235	415	35	24	6158	3	0	t
105236	415	35	25	6158	0	2	t
105185	415	34	24	6157	3	0	f
105312	415	37	1	6160	3	0	t
105263	415	36	2	6159	0	1	t
105264	415	36	3	6159	1	3	t
105213	415	35	2	6158	0	2	t
105215	415	35	4	6158	1	0	t
105266	415	36	5	6159	0	1	t
105265	415	36	4	6159	3	0	t
105186	415	34	25	6157	3	1	t
105216	415	35	5	6158	0	2	t
105167	415	34	6	6157	0	1	f
105168	415	34	7	6157	0	2	f
105267	415	36	6	6159	1	3	t
105169	415	34	8	6157	0	1	t
105318	415	37	7	6160	3	1	f
105187	415	34	26	6157	1	0	t
105219	415	35	8	6158	0	2	t
105319	415	37	8	6160	3	0	t
105170	415	34	9	6157	1	2	t
105220	415	35	9	6158	3	2	t
105321	415	37	10	6160	3	0	t
105322	415	37	11	6160	0	2	f
105271	415	36	10	6159	1	2	t
105221	415	35	10	6158	3	1	f
105223	415	35	12	6158	0	2	t
105272	415	36	11	6159	3	1	f
105174	415	34	13	6157	3	0	t
105173	415	34	12	6157	1	2	t
105273	415	36	12	6159	3	2	t
105224	415	35	13	6158	3	2	t
105274	415	36	13	6159	3	2	t
105237	415	35	26	6158	3	1	t
105188	415	34	27	6157	0	2	t
105287	415	36	26	6159	3	2	t
105189	415	34	28	6157	3	0	t
105238	415	35	27	6158	1	2	t
105240	415	35	29	6158	0	2	t
105239	415	35	28	6158	3	0	t
105191	415	34	30	6157	0	1	t
105190	415	34	29	6157	0	2	f
105253	415	35	42	6158	1	2	t
105204	415	34	43	6157	0	2	t
105291	415	36	30	6159	3	0	t
105255	415	35	44	6158	0	1	t
105254	415	35	43	6158	3	0	t
105305	415	36	44	6159	3	1	t
105256	415	35	45	6158	1	2	t
105307	415	36	46	6159	3	0	t
105306	415	36	45	6159	1	3	t
105308	415	36	47	6159	0	1	t
105257	415	35	46	6158	3	1	t
105258	415	35	47	6158	1	2	t
105342	415	37	31	6160	0	2	t
105393	415	38	32	6161	0	2	t
105442	415	39	31	6162	3	2	t
105343	415	37	32	6160	3	0	t
105344	415	37	33	6160	0	1	t
104893	415	28	32	6151	3	1	t
105359	415	37	48	6160	1	0	f
105394	415	38	33	6161	3	0	t
105345	415	37	34	6160	1	0	f
105395	415	38	34	6161	0	2	t
105409	415	38	48	6161	3	2	t
105360	415	37	49	6160	1	2	t
105460	415	39	49	6162	3	2	f
105410	415	38	49	6161	3	2	f
108319	417	27	8	6220	3	1	f
105476	416	0	15	6163	0	2	t
105375	415	38	14	6161	3	0	t
105376	415	38	15	6161	0	2	t
105425	415	39	14	6162	1	2	t
105325	415	37	14	6160	1	2	t
105346	415	37	35	6160	1	0	t
105426	415	39	15	6162	3	0	t
105427	415	39	16	6162	0	2	t
104976	415	30	15	6153	3	0	t
105447	415	39	36	6162	0	1	t
105396	415	38	35	6161	3	0	t
105347	415	37	36	6160	0	2	t
105397	415	38	36	6161	0	2	f
105448	415	39	37	6162	1	2	t
105349	415	37	38	6160	1	2	t
105348	415	37	37	6160	3	1	t
105478	416	0	17	6163	0	2	t
105399	415	38	38	6161	3	1	t
105400	415	38	39	6161	1	2	t
105479	416	0	18	6163	0	2	t
105378	415	38	17	6161	1	2	t
105377	415	38	16	6161	3	1	t
105379	415	38	18	6161	3	0	t
105328	415	37	17	6160	1	2	t
105428	415	39	17	6162	3	2	t
105380	415	38	19	6161	0	2	t
105329	415	37	18	6160	3	2	f
105351	415	37	40	6160	1	2	t
105350	415	37	39	6160	3	1	t
105352	415	37	41	6160	3	0	t
105401	415	38	40	6161	3	1	t
105451	415	39	40	6162	3	2	t
105402	415	38	41	6161	1	2	t
105353	415	37	42	6160	0	2	t
105403	415	38	42	6161	3	2	t
105331	415	37	20	6160	0	2	f
105330	415	37	19	6160	3	0	t
105430	415	39	19	6162	3	2	t
105404	415	38	43	6161	3	0	t
105381	415	38	20	6161	3	1	t
105332	415	37	21	6160	0	2	t
105382	415	38	21	6161	1	2	t
105333	415	37	22	6160	3	1	t
105367	415	38	6	6161	0	2	f
105413	415	39	2	6162	1	2	t
105363	415	38	2	6161	3	0	t
105364	415	38	3	6161	0	2	t
105365	415	38	4	6161	3	1	f
105414	415	39	3	6162	3	0	t
105415	415	39	4	6162	0	2	t
105366	415	38	5	6161	3	0	t
105416	415	39	5	6162	3	1	t
105417	415	39	6	6162	1	2	t
105368	415	38	7	6161	0	2	t
105418	415	39	7	6162	3	0	t
105419	415	39	8	6162	0	2	t
105420	415	39	9	6162	3	1	t
105369	415	38	8	6161	3	2	t
105421	415	39	10	6162	1	2	t
105370	415	38	9	6161	3	2	t
105371	415	38	10	6161	3	2	f
105372	415	38	11	6161	3	1	f
105422	415	39	11	6162	3	2	t
105323	415	37	12	6160	0	1	t
105373	415	38	12	6161	3	0	t
105423	415	39	12	6162	3	2	t
105374	415	38	13	6161	0	2	t
105324	415	37	13	6160	1	2	f
105383	415	38	22	6161	3	2	t
105424	415	39	13	6162	3	1	t
105434	415	39	23	6162	3	0	t
105334	415	37	23	6160	1	2	t
105354	415	37	43	6160	3	1	t
105435	415	39	24	6162	0	1	t
105335	415	37	24	6160	3	0	f
105436	415	39	25	6162	1	2	t
105337	415	37	26	6160	1	2	t
105336	415	37	25	6160	3	1	t
105355	415	37	44	6160	1	0	t
105437	415	39	26	6162	3	2	t
105338	415	37	27	6160	3	1	f
105438	415	39	27	6162	3	2	t
105389	415	38	28	6161	0	2	t
105339	415	37	28	6160	3	1	t
105340	415	37	29	6160	1	0	t
105390	415	38	29	6161	3	1	f
105341	415	37	30	6160	0	2	f
105441	415	39	30	6162	3	2	t
105405	415	38	44	6161	0	2	t
105456	415	39	45	6162	0	2	t
105358	415	37	47	6160	1	0	f
105356	415	37	45	6160	0	2	t
105357	415	37	46	6160	3	1	t
105457	415	39	46	6162	3	2	t
105408	415	38	47	6161	3	2	t
104161	415	14	0	6137	1	0	t
103811	415	7	0	6130	0	1	t
104211	415	15	0	6138	1	0	t
103761	415	6	0	6129	0	1	t
103611	415	3	0	6126	0	1	f
103511	415	1	0	6124	0	1	f
104661	415	24	0	6147	2	0	t
103461	415	0	0	6123	0	2	t
104761	415	26	0	6149	2	0	t
104911	415	29	0	6152	2	0	f
104561	415	22	0	6145	2	0	f
103911	415	9	0	6132	0	3	t
104826	415	27	15	6150	2	0	f
105276	415	36	15	6159	3	2	t
105361	415	38	0	6161	3	0	t
103711	415	5	0	6128	0	3	t
104877	415	28	16	6151	2	1	t
105061	415	32	0	6155	3	0	t
103661	415	4	0	6127	0	3	t
104277	415	16	16	6139	1	2	t
103861	415	8	0	6131	0	3	f
104127	415	13	16	6136	2	1	f
104461	415	20	0	6143	2	1	t
103961	415	10	0	6133	1	2	t
104861	415	28	0	6151	2	1	t
104411	415	19	0	6142	1	2	t
104677	415	24	16	6147	2	1	f
104611	415	23	0	6146	2	1	t
104111	415	13	0	6136	1	2	t
104427	415	19	16	6142	1	3	t
104511	415	21	0	6144	2	1	t
104261	415	16	0	6139	1	2	t
104361	415	18	0	6141	1	2	f
104311	415	17	0	6140	1	2	f
104827	415	27	16	6150	2	3	t
104011	415	11	0	6134	1	2	f
104061	415	12	0	6135	1	3	t
105111	415	33	0	6156	3	1	t
105411	415	39	0	6162	3	1	f
105311	415	37	0	6160	3	1	f
104811	415	27	0	6150	2	3	t
104961	415	30	0	6153	3	2	t
104711	415	25	0	6148	2	3	t
105261	415	36	0	6159	3	2	t
105011	415	31	0	6154	3	2	f
105211	415	35	0	6158	3	2	f
104362	415	18	1	6141	1	0	t
104312	415	17	1	6140	1	0	t
105062	415	32	1	6155	0	1	t
104012	415	11	1	6134	1	0	t
103612	415	3	1	6126	0	2	t
104112	415	13	1	6136	2	0	t
105162	415	34	1	6157	0	2	t
105362	415	38	1	6161	0	2	t
104612	415	23	1	6146	2	0	f
103912	415	9	1	6132	0	3	t
105262	415	36	1	6159	3	0	t
103712	415	5	1	6128	0	3	t
105212	415	35	1	6158	3	0	t
103512	415	1	1	6124	0	3	t
104812	415	27	1	6150	3	0	t
103862	415	8	1	6131	0	3	t
104062	415	12	1	6135	3	0	t
103662	415	4	1	6127	0	3	t
104562	415	22	1	6145	2	1	t
104212	415	15	1	6138	1	2	t
105112	415	33	1	6156	1	2	t
104862	415	28	1	6151	2	1	t
104512	415	21	1	6144	2	1	f
105412	415	39	1	6162	3	1	t
104712	415	25	1	6148	3	1	t
105012	415	31	1	6154	3	1	f
104962	415	30	1	6153	3	2	t
104412	415	19	1	6142	2	3	f
104278	415	16	17	6139	2	0	f
104128	415	13	17	6136	2	0	f
103528	415	1	17	6124	0	3	t
105313	415	37	2	6160	0	2	t
104428	415	19	17	6142	3	0	t
104878	415	28	17	6151	2	1	t
103628	415	3	17	6126	1	3	t
103863	415	8	2	6131	0	3	t
103480	415	0	19	6123	1	2	t
103813	415	7	2	6130	0	3	f
104030	415	11	19	6134	1	2	t
105063	415	32	2	6155	1	2	t
104163	415	14	2	6137	2	1	f
105080	415	32	19	6155	3	2	t
104463	415	20	2	6143	2	1	f
103463	415	0	2	6123	2	1	f
105163	415	34	2	6157	3	1	t
104313	415	17	2	6140	1	3	t
103963	415	10	2	6133	1	3	f
104963	415	30	2	6153	3	2	t
104563	415	22	2	6145	2	3	f
104331	415	17	20	6140	1	0	t
104763	415	26	2	6149	2	3	f
103613	415	3	2	6126	2	3	f
103532	415	1	21	6124	0	3	t
104133	415	13	22	6136	1	0	f
103933	415	9	22	6132	0	3	f
103484	415	0	23	6123	2	3	t
104064	415	12	3	6135	1	0	f
104364	415	18	3	6141	1	0	f
104164	415	14	3	6137	2	0	t
104214	415	15	3	6138	2	0	t
104664	415	24	3	6147	2	0	t
103814	415	7	3	6130	0	2	t
103864	415	8	3	6131	0	3	t
104314	415	17	3	6140	3	0	t
103914	415	9	3	6132	0	3	f
104564	415	22	3	6145	2	1	t
105164	415	34	3	6157	1	2	t
104464	415	20	3	6143	2	1	f
104714	415	25	3	6148	3	1	t
104414	415	19	3	6142	1	3	t
105064	415	32	3	6155	3	1	t
105314	415	37	3	6160	3	1	t
105214	415	35	3	6158	3	1	t
103964	415	10	3	6133	1	3	t
103514	415	1	3	6124	1	3	f
104964	415	30	3	6153	3	2	t
104764	415	26	3	6149	2	3	t
103614	415	3	3	6126	2	3	f
104914	415	29	3	6152	2	3	f
103965	415	10	4	6133	3	0	t
104376	415	18	15	6141	1	0	t
103615	415	3	4	6126	2	1	t
105315	415	37	4	6160	1	2	t
104476	415	20	15	6143	2	1	f
103778	415	6	17	6129	1	3	f
104615	415	23	4	6146	2	1	t
106289	416	16	28	6179	2	0	t
104915	415	29	4	6152	2	1	t
104165	415	14	4	6137	1	2	t
105193	415	34	32	6157	3	1	t
103465	415	0	4	6123	2	1	t
104365	415	18	4	6141	1	2	t
104678	415	24	17	6147	2	3	t
105115	415	33	4	6156	3	1	f
105278	415	36	17	6159	3	2	t
104715	415	25	4	6148	2	3	f
104828	415	27	17	6150	3	2	t
104465	415	20	4	6143	2	3	f
103815	415	7	4	6130	2	3	f
103966	415	10	5	6133	1	0	f
104166	415	14	5	6137	2	0	t
104916	415	29	5	6152	2	0	t
104716	415	25	5	6148	2	0	t
104466	415	20	5	6143	2	0	f
105166	415	34	5	6157	3	0	t
103916	415	9	5	6132	0	3	f
103616	415	3	5	6126	1	3	t
105316	415	37	5	6160	3	1	t
105116	415	33	5	6156	3	2	t
104616	415	23	5	6146	2	3	f
103816	415	7	5	6130	2	3	f
104366	415	18	5	6141	2	3	f
103979	415	10	18	6133	1	0	t
103667	415	4	6	6127	0	3	t
103479	415	0	18	6123	0	1	t
103467	415	0	6	6123	0	3	f
105429	415	39	18	6162	3	1	f
103817	415	7	6	6130	2	1	t
105317	415	37	6	6160	1	2	t
104667	415	24	6	6147	2	1	t
104067	415	12	6	6135	1	2	t
104031	415	11	20	6134	2	0	t
104817	415	27	6	6150	3	1	t
104167	415	14	6	6137	1	3	t
104317	415	17	6	6140	1	3	f
104967	415	30	6	6153	3	2	t
103517	415	1	6	6124	2	3	t
105217	415	35	6	6158	3	2	t
104517	415	21	6	6144	2	3	t
104233	415	15	22	6138	1	0	t
104318	415	17	7	6140	1	0	f
104668	415	24	7	6147	2	0	t
105268	415	36	7	6159	3	0	t
103668	415	4	7	6127	0	3	t
105218	415	35	7	6158	3	0	t
103518	415	1	7	6124	0	3	t
103918	415	9	7	6132	0	3	f
103818	415	7	7	6130	1	3	t
104518	415	21	7	6144	3	1	t
104168	415	14	7	6137	3	1	f
104968	415	30	7	6153	3	2	t
104068	415	12	7	6135	2	3	f
104818	415	27	7	6150	2	3	f
104069	415	12	8	6135	2	0	t
103919	415	9	8	6132	0	3	t
105269	415	36	8	6159	0	3	f
104219	415	15	8	6138	1	2	t
104619	415	23	8	6146	2	1	t
103619	415	3	8	6126	2	1	f
103469	415	0	8	6123	2	1	f
104369	415	18	8	6141	1	3	t
104419	415	19	8	6142	1	3	f
104969	415	30	8	6153	3	2	t
104819	415	27	8	6150	2	3	t
105019	415	31	8	6154	3	2	f
105270	415	36	9	6159	0	1	t
104070	415	12	9	6135	1	0	t
105320	415	37	9	6160	0	2	t
104220	415	15	9	6138	2	0	f
104820	415	27	9	6150	3	0	t
103520	415	1	9	6124	0	3	t
104370	415	18	9	6141	3	0	t
103920	415	9	9	6132	0	3	f
104420	415	19	9	6142	1	2	t
104620	415	23	9	6146	2	1	t
105020	415	31	9	6154	3	2	t
103620	415	3	9	6126	2	3	t
104970	415	30	9	6153	3	2	t
103471	415	0	10	6123	0	1	t
104321	415	17	10	6140	2	0	t
104171	415	14	10	6137	3	0	t
103921	415	9	10	6132	0	3	t
103621	415	3	10	6126	0	3	f
104671	415	24	10	6147	2	1	t
103821	415	7	10	6130	1	2	f
104721	415	25	10	6148	3	1	f
104471	415	20	10	6143	2	3	t
104971	415	30	10	6153	3	2	t
105171	415	34	10	6157	3	2	f
105021	415	31	10	6154	3	2	f
103622	415	3	11	6126	0	1	t
104322	415	17	11	6140	1	0	t
103522	415	1	11	6124	0	1	t
104022	415	11	11	6134	2	0	t
105222	415	35	11	6158	3	0	t
103922	415	9	11	6132	0	3	t
104172	415	14	11	6137	1	2	t
103472	415	0	11	6123	1	2	t
104672	415	24	11	6147	2	1	t
103822	415	7	11	6130	1	3	t
105172	415	34	11	6157	3	1	t
104722	415	25	11	6148	3	1	t
104472	415	20	11	6143	3	1	f
105022	415	31	11	6154	3	2	t
104972	415	30	11	6153	3	2	t
103823	415	7	12	6130	0	2	t
103525	415	1	14	6124	0	3	t
103825	415	7	14	6130	0	3	t
103475	415	0	14	6123	2	1	t
104173	415	14	12	6137	2	1	f
105025	415	31	14	6154	3	2	t
104423	415	19	12	6142	1	3	t
105275	415	36	14	6159	3	2	f
103623	415	3	12	6126	1	3	t
103526	415	1	15	6124	0	2	t
104323	415	17	12	6140	1	3	t
105489	416	0	28	6163	0	2	f
103973	415	10	12	6133	1	3	f
105293	415	36	32	6159	1	3	t
103523	415	1	12	6124	1	3	f
104973	415	30	12	6153	3	2	t
103826	415	7	15	6130	0	3	t
104623	415	23	12	6146	2	3	t
104226	415	15	15	6138	3	0	t
104723	415	25	12	6148	2	3	t
104943	415	29	32	6152	3	1	t
105023	415	31	12	6154	3	2	t
103473	415	0	12	6123	2	3	f
104224	415	15	13	6138	1	0	t
104474	415	20	13	6143	0	1	t
103974	415	10	13	6133	1	0	t
104274	415	16	13	6139	2	0	t
103624	415	3	13	6126	0	2	t
104324	415	17	13	6140	3	0	t
103924	415	9	13	6132	0	3	t
104424	415	19	13	6142	3	0	t
104574	415	22	13	6145	2	1	t
108719	417	35	8	6228	3	1	f
104624	415	23	13	6146	3	1	t
104974	415	30	13	6153	3	1	f
104724	415	25	13	6148	3	1	f
105024	415	31	13	6154	3	2	t
104174	415	14	13	6137	2	3	t
103824	415	7	13	6130	2	3	t
104993	415	30	32	6153	3	1	f
105043	415	31	32	6154	3	2	t
104774	415	26	13	6149	2	3	f
105326	415	37	15	6160	3	0	f
103593	415	2	32	6125	2	3	t
105485	416	0	24	6163	0	2	t
105026	415	31	15	6154	3	2	f
105194	415	34	33	6157	1	0	f
103577	415	2	16	6125	0	2	t
103977	415	10	16	6133	2	0	t
103827	415	7	16	6130	0	3	t
103477	415	0	16	6123	1	2	t
105327	415	37	16	6160	3	1	t
105277	415	36	16	6159	3	2	t
103527	415	1	16	6124	2	3	t
105027	415	31	16	6154	3	2	t
103729	415	5	18	6128	0	3	t
104229	415	15	18	6138	1	2	t
105279	415	36	18	6159	3	2	t
105029	415	31	18	6154	3	2	f
104230	415	15	19	6138	2	0	t
104330	415	17	19	6140	3	0	t
103880	415	8	19	6131	0	3	t
104630	415	23	19	6146	3	0	t
103730	415	5	19	6128	0	3	t
104530	415	21	19	6144	2	1	t
104780	415	26	19	6149	2	1	t
104880	415	28	19	6151	2	1	t
103530	415	1	19	6124	2	3	t
105280	415	36	19	6159	3	2	t
104281	415	16	20	6139	1	0	f
103581	415	2	20	6125	0	2	t
103531	415	1	20	6124	0	3	f
104531	415	21	20	6144	2	1	f
104681	415	24	20	6147	2	1	f
103831	415	7	20	6130	1	3	t
105081	415	32	20	6155	3	1	f
104831	415	27	20	6150	2	3	t
105431	415	39	20	6162	3	2	t
104981	415	30	20	6153	3	2	f
105281	415	36	20	6159	3	2	f
104282	415	16	21	6139	1	0	t
103482	415	0	21	6123	0	1	t
103832	415	7	21	6130	0	3	t
104982	415	30	21	6153	3	0	t
104832	415	27	21	6150	3	0	t
103682	415	4	21	6127	0	3	f
104682	415	24	21	6147	2	1	f
104532	415	21	21	6144	2	1	f
105432	415	39	21	6162	3	2	f
105282	415	36	21	6159	3	2	f
103533	415	1	22	6124	0	2	f
103633	415	3	22	6126	1	3	t
105083	415	32	22	6155	3	2	t
105433	415	39	22	6162	3	2	f
103634	415	3	23	6126	0	1	t
103884	415	8	23	6131	0	2	t
104284	415	16	23	6139	2	0	f
103934	415	9	23	6132	0	3	t
104285	415	16	24	6139	2	0	t
103935	415	9	24	6132	0	3	t
103534	415	1	23	6124	0	3	t
105488	416	0	27	6163	0	2	f
105234	415	35	23	6158	1	2	t
104134	415	13	23	6136	1	3	t
105292	415	36	31	6159	0	1	t
104634	415	23	23	6146	3	1	f
104934	415	29	23	6152	3	1	f
104484	415	20	23	6143	3	1	f
104734	415	25	23	6148	2	3	t
105034	415	31	23	6154	3	2	t
103992	415	10	31	6133	2	0	t
104442	415	19	31	6142	3	0	t
105384	415	38	23	6161	3	2	t
108892	417	38	31	6231	2	1	f
103535	415	1	24	6124	0	2	t
103585	415	2	24	6125	0	2	t
105443	415	39	32	6162	3	2	t
104135	415	13	24	6136	3	0	t
104885	415	28	24	6151	2	1	t
104635	415	23	24	6146	3	1	t
103543	415	1	32	6124	2	3	f
104543	415	21	32	6144	2	3	f
105285	415	36	24	6159	1	3	t
104485	415	20	24	6143	3	1	f
105385	415	38	24	6161	3	2	t
103885	415	8	24	6131	2	3	t
105035	415	31	24	6154	3	2	t
104835	415	27	24	6150	2	3	t
104544	415	21	33	6144	2	0	t
104286	415	16	25	6139	1	0	t
103886	415	8	25	6131	0	2	t
104636	415	23	25	6146	2	0	t
103636	415	3	25	6126	0	2	t
104486	415	20	25	6143	3	0	t
104836	415	27	25	6150	3	0	t
104894	415	28	33	6151	2	1	f
103486	415	0	25	6123	1	2	t
104886	415	28	25	6151	2	1	t
106839	416	27	28	6190	2	1	t
104136	415	13	25	6136	1	3	t
105286	415	36	25	6159	3	2	t
105386	415	38	25	6161	3	2	t
104137	415	13	26	6136	3	0	t
104337	415	17	26	6140	3	0	t
103537	415	1	26	6124	0	3	t
103937	415	9	26	6132	0	3	f
104587	415	22	26	6145	2	1	t
104737	415	25	26	6148	3	1	t
104437	415	19	26	6142	1	3	t
105037	415	31	26	6154	3	2	t
103637	415	3	26	6126	2	3	t
103887	415	8	26	6131	2	3	t
105387	415	38	26	6161	3	2	f
104987	415	30	26	6153	3	2	f
103638	415	3	27	6126	0	1	t
104538	415	21	27	6144	0	1	t
104238	415	15	27	6138	2	0	t
103488	415	0	27	6123	0	2	t
104438	415	19	27	6142	3	0	t
104988	415	30	27	6153	3	0	t
105388	415	38	27	6161	3	0	t
104038	415	11	27	6134	1	2	t
104588	415	22	27	6145	2	1	t
103838	415	7	27	6130	1	3	t
105038	415	31	27	6154	3	2	t
103588	415	2	27	6125	2	3	t
104738	415	25	27	6148	2	3	t
105288	415	36	27	6159	3	2	t
104088	415	12	27	6135	2	3	t
104239	415	15	28	6138	1	0	f
104039	415	11	28	6134	2	0	f
104089	415	12	28	6135	3	0	t
103839	415	7	28	6130	0	3	f
103939	415	9	28	6132	0	3	f
104439	415	19	28	6142	1	2	t
104539	415	21	28	6144	2	1	t
104589	415	22	28	6145	2	1	t
104889	415	28	28	6151	2	1	f
103639	415	3	28	6126	1	3	t
105289	415	36	28	6159	3	2	t
103539	415	1	28	6124	2	3	t
105439	415	39	28	6162	3	2	t
104789	415	26	28	6149	2	3	t
105089	415	32	28	6155	3	2	t
105039	415	31	28	6154	3	2	t
104290	415	16	29	6139	2	0	t
104440	415	19	29	6142	2	0	t
103490	415	0	29	6123	0	2	t
103640	415	3	29	6126	0	2	f
103840	415	7	29	6130	0	3	t
103690	415	4	29	6127	0	3	f
103940	415	9	29	6132	0	3	f
104540	415	21	29	6144	2	1	t
104890	415	28	29	6151	2	1	f
104590	415	22	29	6145	2	1	f
104090	415	12	29	6135	1	3	t
105440	415	39	29	6162	3	2	t
104790	415	26	29	6149	3	2	t
105040	415	31	29	6154	3	2	f
105290	415	36	29	6159	3	2	f
104291	415	16	30	6139	1	0	t
103591	415	2	30	6125	0	2	t
104091	415	12	30	6135	3	0	t
103841	415	7	30	6130	0	3	f
103691	415	4	30	6127	0	3	f
103991	415	10	30	6133	1	2	t
104591	415	22	30	6145	2	1	f
104991	415	30	30	6153	3	1	t
104441	415	19	30	6142	1	3	t
105241	415	35	30	6158	3	1	f
105041	415	31	30	6154	3	2	t
104841	415	27	30	6150	2	3	t
105391	415	38	30	6161	3	2	t
103491	415	0	30	6123	2	3	t
105392	415	38	31	6161	3	0	t
104344	415	17	33	6140	1	3	f
107869	417	18	8	6211	3	1	f
104244	415	15	33	6138	1	3	f
103544	415	1	33	6124	2	3	t
104994	415	30	33	6153	3	2	t
105044	415	31	33	6154	3	2	t
105294	415	36	33	6159	3	2	f
105444	415	39	33	6162	3	2	f
104245	415	15	34	6138	1	0	f
103545	415	1	34	6124	0	3	f
104345	415	17	34	6140	1	3	t
104645	415	23	34	6146	3	1	t
105295	415	36	34	6159	3	1	t
104145	415	13	34	6136	1	3	t
104745	415	25	34	6148	3	1	t
103645	415	3	34	6126	2	3	t
105493	416	0	32	6163	0	2	f
103595	415	2	34	6125	2	3	t
105495	416	0	34	6163	0	2	f
103495	415	0	34	6123	2	3	t
105045	415	31	34	6154	3	2	f
103646	415	3	35	6126	0	1	t
105496	416	0	35	6163	0	2	t
103596	415	2	35	6125	0	2	f
103546	415	1	35	6124	0	3	t
105498	416	0	37	6163	0	2	t
103946	415	9	35	6132	0	3	t
103696	415	4	35	6127	0	3	t
103996	415	10	35	6133	3	0	t
104146	415	13	35	6136	3	0	t
104446	415	19	35	6142	3	0	f
104246	415	15	35	6138	1	2	t
104646	415	23	35	6146	2	1	t
104746	415	25	35	6148	2	3	t
105046	415	31	35	6154	3	2	t
104996	415	30	35	6153	3	2	t
103797	415	6	36	6129	0	2	t
104247	415	15	36	6138	2	0	t
103547	415	1	36	6124	0	3	t
103697	415	4	36	6127	0	3	t
103597	415	2	36	6125	0	3	f
104547	415	21	36	6144	3	1	t
104747	415	25	36	6148	3	1	t
105247	415	35	36	6158	3	1	t
103497	415	0	36	6123	2	3	t
104947	415	29	36	6152	2	3	t
104198	415	14	37	6137	1	0	t
104498	415	20	37	6143	2	0	t
105398	415	38	37	6161	0	2	t
104548	415	21	37	6144	2	1	t
104948	415	29	37	6152	3	1	f
105298	415	36	37	6159	3	2	t
105048	415	31	37	6154	3	2	t
104748	415	25	37	6148	2	3	f
103499	415	0	38	6123	0	1	t
103799	415	6	38	6129	0	1	t
104449	415	19	38	6142	2	0	f
104349	415	17	38	6140	1	2	t
104749	415	25	38	6148	2	3	t
105449	415	39	38	6162	3	2	t
105299	415	36	38	6159	3	2	f
105049	415	31	38	6154	3	2	f
104050	415	11	39	6134	1	0	f
103650	415	3	39	6126	0	2	t
103550	415	1	39	6124	0	2	t
104450	415	19	39	6142	2	0	f
104350	415	17	39	6140	2	0	f
104150	415	13	39	6136	3	0	t
105000	415	30	39	6153	3	0	t
103800	415	6	39	6129	1	3	t
104750	415	25	39	6148	3	1	t
105050	415	31	39	6154	3	2	t
105450	415	39	39	6162	3	2	f
103801	415	6	40	6129	0	2	t
104351	415	17	40	6140	2	0	f
103501	415	0	40	6123	0	3	f
105301	415	36	40	6159	3	1	t
104851	415	27	40	6150	3	1	t
104101	415	12	40	6135	1	3	t
104951	415	29	40	6152	3	1	f
103551	415	1	40	6124	2	3	t
104651	415	23	40	6146	2	3	t
103652	415	3	41	6126	0	3	t
104102	415	12	41	6135	3	0	t
103952	415	9	41	6132	0	3	f
104652	415	23	41	6146	3	1	t
104452	415	19	41	6142	1	3	t
104752	415	25	41	6148	3	1	t
105202	415	34	41	6157	3	2	f
104952	415	29	41	6152	3	2	f
105052	415	31	41	6154	3	2	f
105452	415	39	41	6162	3	2	f
103603	415	2	42	6125	0	1	t
104653	415	23	42	6146	2	0	t
104303	415	16	42	6139	2	0	t
104453	415	19	42	6142	3	0	t
103953	415	9	42	6132	0	3	t
105203	415	34	42	6157	3	0	t
103703	415	4	42	6127	0	3	f
103503	415	0	42	6123	1	3	t
103803	415	6	42	6129	1	3	f
104753	415	25	42	6148	2	3	t
105103	415	32	42	6155	3	2	t
103704	415	4	43	6127	0	1	t
104154	415	13	43	6136	1	0	f
104954	415	29	43	6152	2	0	t
103954	415	9	43	6132	0	3	t
104454	415	19	43	6142	1	2	t
104754	415	25	43	6148	3	1	t
105453	415	39	42	6162	3	2	f
103504	415	0	43	6123	0	1	t
104554	415	21	43	6144	2	1	f
104359	415	17	48	6140	2	0	t
105304	415	36	43	6159	1	3	t
103604	415	2	43	6125	1	3	t
103909	415	8	48	6131	0	3	f
103804	415	6	43	6129	1	3	f
104609	415	22	48	6145	2	1	f
104509	415	20	48	6143	2	1	f
104354	415	17	43	6140	2	3	t
104759	415	25	48	6148	3	1	t
103509	415	0	48	6123	2	3	t
105104	415	32	43	6155	3	2	f
105454	415	39	43	6162	3	2	f
103605	415	2	44	6125	0	1	t
104455	415	19	44	6142	2	0	t
104555	415	21	44	6144	2	0	f
105455	415	39	44	6162	3	0	t
104355	415	17	44	6140	3	0	t
103955	415	9	44	6132	0	3	t
105459	415	39	48	6162	3	2	t
103805	415	6	44	6129	1	3	t
105205	415	34	44	6157	3	1	t
103705	415	4	44	6127	1	3	t
105059	415	31	48	6154	3	2	f
107769	417	16	8	6209	2	3	t
104705	415	24	44	6147	3	1	t
104155	415	13	44	6136	1	3	t
109369	417	48	8	6241	3	2	t
105055	415	31	44	6154	3	2	t
105005	415	30	44	6153	3	2	t
104256	415	15	45	6138	2	0	t
104156	415	13	45	6136	3	0	t
103956	415	9	45	6132	0	3	t
104856	415	27	45	6150	3	0	t
103706	415	4	45	6127	0	3	f
105206	415	34	45	6157	1	2	t
104606	415	22	45	6145	2	1	t
103506	415	0	45	6123	1	2	t
104756	415	25	45	6148	3	1	t
105406	415	38	45	6161	3	1	t
104456	415	19	45	6142	1	3	f
103906	415	8	45	6131	2	3	t
105006	415	30	45	6153	3	2	t
105056	415	31	45	6154	3	2	f
105537	416	1	26	6164	0	2	t
104257	415	15	46	6138	1	0	t
103907	415	8	46	6131	0	2	t
105539	416	1	28	6164	0	2	f
105407	415	38	46	6161	1	2	t
104057	415	11	46	6134	1	2	t
104907	415	28	46	6151	2	1	t
104457	415	19	46	6142	1	2	t
105540	416	1	29	6164	0	2	t
104607	415	22	46	6145	2	1	t
105007	415	30	46	6153	3	1	t
104157	415	13	46	6136	1	3	t
105542	416	1	31	6164	0	2	t
103657	415	3	46	6126	1	3	t
105207	415	34	46	6157	3	2	t
105543	416	1	32	6164	0	2	f
105057	415	31	46	6154	3	2	t
104757	415	25	46	6148	2	3	t
103658	415	3	47	6126	0	2	t
104058	415	11	47	6134	2	0	t
104158	415	13	47	6136	3	0	t
103758	415	5	47	6128	0	3	t
105208	415	34	47	6157	3	0	t
104608	415	22	47	6145	2	1	t
105544	416	1	33	6164	0	2	t
104358	415	17	47	6140	1	2	t
104908	415	28	47	6151	2	1	t
105008	415	30	47	6153	1	2	t
104508	415	20	47	6143	3	1	t
105546	416	1	35	6164	0	2	t
104758	415	25	47	6148	3	1	f
103908	415	8	47	6131	2	3	t
105499	416	0	38	6163	0	2	f
105058	415	31	47	6154	3	2	t
105458	415	39	47	6162	3	2	f
105500	416	0	39	6163	0	2	t
105502	416	0	41	6163	0	2	f
105503	416	0	42	6163	0	2	t
105504	416	0	43	6163	0	2	f
105506	416	0	45	6163	0	2	t
105507	416	0	46	6163	0	2	t
105508	416	0	47	6163	0	2	t
105511	416	1	0	6164	0	2	t
105512	416	1	1	6164	0	2	t
105513	416	1	2	6164	0	1	t
105514	416	1	3	6164	1	2	t
105515	416	1	4	6164	0	2	t
105516	416	1	5	6164	0	2	f
105517	416	1	6	6164	0	1	f
105518	416	1	7	6164	0	1	t
105519	416	1	8	6164	1	2	t
105520	416	1	9	6164	0	2	t
105521	416	1	10	6164	0	2	t
105522	416	1	11	6164	0	2	f
105523	416	1	12	6164	0	1	t
105524	416	1	13	6164	1	2	t
105525	416	1	14	6164	0	2	t
105526	416	1	15	6164	0	2	t
105527	416	1	16	6164	0	2	f
105528	416	1	17	6164	0	2	t
105529	416	1	18	6164	0	2	f
105530	416	1	19	6164	0	1	t
105531	416	1	20	6164	1	2	t
105532	416	1	21	6164	0	2	t
105533	416	1	22	6164	0	2	t
105534	416	1	23	6164	0	2	t
105536	416	1	25	6164	0	2	f
105510	416	0	49	6163	0	2	t
105587	416	2	26	6165	0	1	t
105637	416	3	26	6166	0	2	t
107792	417	16	31	6209	2	3	t
108269	417	26	8	6219	2	3	t
109119	417	43	8	6236	3	2	t
109370	417	48	9	6241	3	2	t
105638	416	3	27	6166	0	2	t
105737	416	5	26	6168	0	2	t
105588	416	2	27	6165	1	2	t
105688	416	4	27	6167	1	2	t
105639	416	3	28	6166	0	2	t
105589	416	2	28	6165	0	2	t
105590	416	2	29	6165	0	1	t
105739	416	5	28	6168	0	2	f
105640	416	3	29	6166	0	2	t
105690	416	4	29	6167	1	2	t
105641	416	3	30	6166	0	2	f
105592	416	2	31	6165	0	1	t
105591	416	2	30	6165	1	2	t
105642	416	3	31	6166	0	2	t
105692	416	4	31	6167	1	2	t
105643	416	3	32	6166	0	2	t
105594	416	2	33	6165	0	2	t
105593	416	2	32	6165	1	2	t
105644	416	3	33	6166	0	2	t
105646	416	3	35	6166	0	2	t
105645	416	3	34	6166	0	2	t
105595	416	2	34	6165	0	2	f
105596	416	2	35	6165	0	2	f
105696	416	4	35	6167	1	2	t
105597	416	2	36	6165	0	2	t
105598	416	2	37	6165	0	1	t
105647	416	3	36	6166	0	2	f
105648	416	3	37	6166	0	2	t
105649	416	3	38	6166	0	2	f
105599	416	2	38	6165	1	2	t
105600	416	2	39	6165	0	1	t
105650	416	3	39	6166	0	2	t
105700	416	4	39	6167	0	2	t
105651	416	3	40	6166	0	2	f
105602	416	2	41	6165	0	2	t
105601	416	2	40	6165	1	2	t
105603	416	2	42	6165	0	2	t
105702	416	4	41	6167	0	2	f
105703	416	4	42	6167	0	2	t
105604	416	2	43	6165	0	2	t
105705	416	4	44	6167	0	2	t
105704	416	4	43	6167	0	2	t
105662	416	4	1	6167	1	2	t
105663	416	4	2	6167	0	2	t
105615	416	3	4	6166	0	2	t
105613	416	3	2	6166	0	2	t
105664	416	4	3	6167	0	1	f
105654	416	3	43	6166	0	2	f
105617	416	3	6	6166	0	1	f
105665	416	4	4	6167	0	2	f
105616	416	3	5	6166	0	2	f
105666	416	4	5	6167	0	2	f
105668	416	4	7	6167	0	1	t
105667	416	4	6	6167	0	2	t
105618	416	3	7	6166	0	1	t
105719	416	5	8	6168	1	0	t
105619	416	3	8	6166	1	2	t
105620	416	3	9	6166	0	1	t
105621	416	3	10	6166	1	0	t
105605	416	2	44	6165	0	2	t
105720	416	5	9	6168	0	2	f
105671	416	4	10	6167	0	1	t
105723	416	5	12	6168	1	0	t
105622	416	3	11	6166	0	2	t
105672	416	4	11	6167	1	2	t
105656	416	3	45	6166	0	2	t
105675	416	4	14	6167	0	1	t
105623	416	3	12	6166	0	2	t
105724	416	5	13	6168	0	2	t
105726	416	5	15	6168	0	2	t
105725	416	5	14	6168	0	2	t
105707	416	4	46	6167	0	2	t
105727	416	5	16	6168	0	2	t
105626	416	3	15	6166	0	2	f
105728	416	5	17	6168	0	2	t
105627	416	3	16	6166	0	2	f
105706	416	4	45	6167	0	2	t
105628	416	3	17	6166	0	2	t
105729	416	5	18	6168	0	2	t
105630	416	3	19	6166	0	2	t
105629	416	3	18	6166	0	2	t
105732	416	5	21	6168	0	2	t
105730	416	5	19	6168	0	2	f
105631	416	3	20	6166	0	2	t
105731	416	5	20	6168	0	2	t
105733	416	5	22	6168	0	2	t
105632	416	3	21	6166	0	2	f
105734	416	5	23	6168	0	1	f
105633	416	3	22	6166	0	2	t
105585	416	2	24	6165	0	1	t
105634	416	3	23	6166	0	2	t
105635	416	3	24	6166	0	2	t
105657	416	3	46	6166	0	2	f
105735	416	5	24	6168	0	2	t
105636	416	3	25	6166	0	2	f
105658	416	3	47	6166	0	2	t
105586	416	2	25	6165	1	2	t
105609	416	2	48	6165	0	2	t
105708	416	4	47	6167	0	2	t
105659	416	3	48	6166	0	2	f
105660	416	3	49	6166	0	2	t
105610	416	2	49	6165	0	2	f
108569	417	32	8	6225	2	3	t
108692	417	34	31	6227	2	3	t
109769	417	56	8	6249	3	2	t
109469	417	50	8	6243	3	2	f
109770	417	56	9	6249	3	2	t
105837	416	7	26	6170	0	1	t
105787	416	6	26	6169	1	2	t
105788	416	6	27	6169	0	1	t
105838	416	7	27	6170	1	0	t
105839	416	7	28	6170	0	2	t
105889	416	8	28	6171	0	2	t
105892	416	8	31	6171	0	1	t
105840	416	7	29	6170	0	2	t
105890	416	8	29	6171	0	2	t
105740	416	5	29	6168	0	2	f
105891	416	8	30	6171	0	2	t
105841	416	7	30	6170	0	2	f
105791	416	6	30	6169	1	2	t
105742	416	5	31	6168	0	2	t
105743	416	5	32	6168	0	2	f
105842	416	7	31	6170	0	2	t
105794	416	6	33	6169	0	1	t
105793	416	6	32	6169	1	2	t
105893	416	8	32	6171	1	2	f
105745	416	5	34	6168	0	2	t
105744	416	5	33	6168	0	2	t
105844	416	7	33	6170	0	2	t
105845	416	7	34	6170	0	2	t
105795	416	6	34	6169	1	2	t
105796	416	6	35	6169	0	1	f
105797	416	6	36	6169	0	1	t
105846	416	7	35	6170	0	2	t
105746	416	5	35	6168	0	2	t
105847	416	7	36	6170	0	2	t
105848	416	7	37	6170	0	2	f
105748	416	5	37	6168	0	2	f
105749	416	5	38	6168	0	1	t
105750	416	5	39	6168	1	0	t
105799	416	6	38	6169	0	1	t
105849	416	7	38	6170	0	2	t
105801	416	6	40	6169	0	1	t
105800	416	6	39	6169	1	2	t
105851	416	7	40	6170	0	2	t
105852	416	7	41	6170	0	2	f
105863	416	8	2	6171	1	0	f
105762	416	6	1	6169	0	1	f
105803	416	6	42	6169	0	1	t
105864	416	8	3	6171	1	0	t
105813	416	7	2	6170	0	2	t
105865	416	8	4	6171	0	2	t
105802	416	6	41	6169	1	2	t
105815	416	7	4	6170	0	2	f
105817	416	7	6	6170	0	1	t
105866	416	8	5	6171	0	2	t
105816	416	7	5	6170	0	2	t
105867	416	8	6	6171	0	2	t
105868	416	8	7	6171	0	2	t
105769	416	6	8	6169	0	1	t
105818	416	7	7	6170	1	2	t
105819	416	7	8	6170	0	1	t
105820	416	7	9	6170	1	0	t
105871	416	8	10	6171	0	2	t
105770	416	6	9	6169	1	2	t
105821	416	7	10	6170	0	2	t
105822	416	7	11	6170	0	1	t
105873	416	8	12	6171	0	2	f
105872	416	8	11	6171	0	2	t
105753	416	5	42	6168	0	2	t
105874	416	8	13	6171	0	1	t
105773	416	6	12	6169	1	2	t
105825	416	7	14	6170	0	2	t
105775	416	6	14	6169	1	2	t
105853	416	7	42	6170	0	2	f
105776	416	6	15	6169	0	1	t
105827	416	7	16	6170	0	2	f
105826	416	7	15	6170	0	2	t
105754	416	5	43	6168	0	2	t
105777	416	6	16	6169	1	2	t
105778	416	6	17	6169	0	1	t
105828	416	7	17	6170	0	2	t
105829	416	7	18	6170	0	2	f
105779	416	6	18	6169	1	2	t
105780	416	6	19	6169	0	1	t
105805	416	6	44	6169	0	1	t
105830	416	7	19	6170	0	2	t
105831	416	7	20	6170	0	1	t
105804	416	6	43	6169	1	2	t
105781	416	6	20	6169	1	2	t
105782	416	6	21	6169	0	1	t
105883	416	8	22	6171	0	2	f
105882	416	8	21	6171	0	2	t
105783	416	6	22	6169	1	2	t
105784	416	6	23	6169	0	1	t
105884	416	8	23	6171	0	2	f
105885	416	8	24	6171	0	2	f
105836	416	7	25	6170	1	0	t
105785	416	6	24	6169	1	2	t
105786	416	6	25	6169	0	1	t
105755	416	5	44	6168	0	2	t
105756	416	5	45	6168	0	2	f
105807	416	6	46	6169	0	1	t
105806	416	6	45	6169	1	2	t
105757	416	5	46	6168	0	2	t
105758	416	5	47	6168	0	2	t
105809	416	6	48	6169	0	1	t
105808	416	6	47	6169	1	2	t
105760	416	5	49	6168	0	2	f
105759	416	5	48	6168	0	2	t
109470	417	50	9	6243	3	2	f
108572	417	32	11	6225	2	3	t
109092	417	42	31	6235	3	2	f
107074	417	2	13	6195	0	3	t
107175	417	4	14	6197	0	2	t
106037	416	11	26	6174	1	0	f
105938	416	9	27	6172	0	1	t
105937	416	9	26	6172	0	2	t
106039	416	11	28	6174	1	0	t
106038	416	11	27	6174	1	0	t
105990	416	10	29	6173	1	0	t
105989	416	10	28	6173	1	0	f
105939	416	9	28	6172	1	2	t
105941	416	9	30	6172	0	1	t
106040	416	11	29	6174	1	2	t
106041	416	11	30	6174	2	0	t
106042	416	11	31	6174	1	0	f
105942	416	9	31	6172	1	2	t
105993	416	10	32	6173	1	0	t
106043	416	11	32	6174	1	0	f
105943	416	9	32	6172	0	2	f
106044	416	11	33	6174	1	2	t
105994	416	10	33	6173	1	2	t
106045	416	11	34	6174	2	0	t
105995	416	10	34	6173	2	0	t
106046	416	11	35	6174	1	0	t
106047	416	11	36	6174	1	0	t
105996	416	10	35	6173	1	2	t
105998	416	10	37	6173	1	0	t
105997	416	10	36	6173	2	0	t
106049	416	11	38	6174	1	0	t
105897	416	8	36	6171	0	2	t
106048	416	11	37	6174	1	0	f
105949	416	9	38	6172	0	1	t
106050	416	11	39	6174	1	0	t
105899	416	8	38	6171	0	2	f
106001	416	10	40	6173	1	0	t
105900	416	8	39	6171	0	2	t
105950	416	9	39	6172	1	2	t
105902	416	8	41	6171	0	2	t
106051	416	11	40	6174	1	0	f
105901	416	8	40	6171	0	2	t
105951	416	9	40	6172	0	2	t
106002	416	10	41	6173	1	2	t
106013	416	11	2	6174	1	0	f
105912	416	9	1	6172	1	2	t
105953	416	9	42	6172	0	1	t
105915	416	9	4	6172	0	1	t
105913	416	9	2	6172	0	2	f
106014	416	11	3	6174	1	2	f
105916	416	9	5	6172	1	2	t
105965	416	10	4	6173	1	0	f
105966	416	10	5	6173	1	2	t
106017	416	11	6	6174	1	0	t
105917	416	9	6	6172	0	1	t
106018	416	11	7	6174	1	0	t
106019	416	11	8	6174	1	0	t
105918	416	9	7	6172	1	2	t
106003	416	10	42	6173	2	0	t
106020	416	11	9	6174	1	0	f
105919	416	9	8	6172	0	1	t
106004	416	10	43	6173	1	0	t
105920	416	9	9	6172	1	2	t
105971	416	10	10	6173	2	0	t
105921	416	9	10	6172	0	2	t
105922	416	9	11	6172	0	2	t
106023	416	11	12	6174	1	0	f
105903	416	8	42	6171	0	2	t
105972	416	10	11	6173	1	2	t
105975	416	10	14	6173	1	0	t
105973	416	10	12	6173	2	0	t
106024	416	11	13	6174	1	2	t
106025	416	11	14	6174	2	0	t
105905	416	8	44	6171	0	1	t
106026	416	11	15	6174	1	0	t
105927	416	9	16	6172	0	1	t
105926	416	9	15	6172	0	2	t
105904	416	8	43	6171	0	2	f
106027	416	11	16	6174	1	2	t
105978	416	10	17	6173	1	0	t
106028	416	11	17	6174	2	0	t
106029	416	11	18	6174	1	0	t
105979	416	10	18	6173	1	0	f
105930	416	9	19	6172	0	1	f
106030	416	11	19	6174	1	2	t
106031	416	11	20	6174	2	0	t
105982	416	10	21	6173	1	0	t
105931	416	9	20	6172	0	2	f
105954	416	9	43	6172	1	2	t
106032	416	11	21	6174	1	0	t
106033	416	11	22	6174	1	0	t
105983	416	10	22	6173	1	2	t
106034	416	11	23	6174	1	0	t
106035	416	11	24	6174	1	0	t
105934	416	9	23	6172	0	1	f
106036	416	11	25	6174	1	0	t
105935	416	9	24	6172	0	2	t
105936	416	9	25	6172	0	2	t
106005	416	10	44	6173	1	2	t
106006	416	10	45	6173	2	0	t
106007	416	10	46	6173	1	0	t
105906	416	8	45	6171	1	2	t
105908	416	8	47	6171	0	2	f
105907	416	8	46	6171	0	2	t
106008	416	10	47	6173	1	2	t
106009	416	10	48	6173	2	0	t
105910	416	8	49	6171	0	2	t
105909	416	8	48	6171	0	2	t
108270	417	26	9	6219	3	0	t
107522	417	11	11	6204	1	0	f
108222	417	25	11	6218	2	0	t
107372	417	8	11	6201	0	3	t
106137	416	13	26	6176	1	0	t
106087	416	12	26	6175	1	0	t
106138	416	13	27	6176	1	0	t
106089	416	12	28	6175	1	0	t
106088	416	12	27	6175	1	0	t
106090	416	12	29	6175	1	0	t
106189	416	14	28	6177	2	0	t
105789	416	6	28	6169	1	2	t
106190	416	14	29	6177	1	0	t
106191	416	14	30	6177	1	0	t
106141	416	13	30	6176	1	0	t
106142	416	13	31	6176	1	0	t
106093	416	12	32	6175	1	0	t
106192	416	14	31	6177	1	0	f
106193	416	14	32	6177	1	2	t
106094	416	12	33	6175	1	0	t
106143	416	13	32	6176	1	2	t
106194	416	14	33	6177	2	0	t
106095	416	12	34	6175	1	0	t
106096	416	12	35	6175	1	0	t
106145	416	13	34	6176	1	0	t
106097	416	12	36	6175	1	0	t
106146	416	13	35	6176	1	2	t
106147	416	13	36	6176	2	0	t
106098	416	12	37	6175	1	0	t
106197	416	14	36	6177	1	2	t
106148	416	13	37	6176	1	0	f
106149	416	13	38	6176	1	0	t
106100	416	12	39	6175	1	0	t
106099	416	12	38	6175	1	0	t
106150	416	13	39	6176	1	2	t
106101	416	12	40	6175	1	0	t
106201	416	14	40	6177	1	0	t
106102	416	12	41	6175	1	0	t
106103	416	12	42	6175	1	0	t
106202	416	14	41	6177	1	0	t
106052	416	11	41	6174	1	0	f
106203	416	14	42	6177	1	0	f
106112	416	13	1	6176	1	0	t
106063	416	12	2	6175	1	0	t
106115	416	13	4	6176	1	0	t
106113	416	13	2	6176	1	2	t
106064	416	12	3	6175	1	2	t
106154	416	13	43	6176	1	0	t
106165	416	14	4	6177	1	0	t
106117	416	13	6	6176	1	0	t
106116	416	13	5	6176	1	0	t
106166	416	14	5	6177	1	0	f
106053	416	11	42	6174	1	2	t
106067	416	12	6	6175	1	2	t
106118	416	13	7	6176	1	0	t
106119	416	13	8	6176	1	0	t
106068	416	12	7	6175	2	1	t
106120	416	13	9	6176	1	0	f
106069	416	12	8	6175	1	0	t
106171	416	14	10	6177	1	0	t
106070	416	12	9	6175	1	2	t
106105	416	12	44	6175	1	0	t
106121	416	13	10	6176	1	2	t
106172	416	14	11	6177	1	0	t
106123	416	13	12	6176	1	0	t
106122	416	13	11	6176	2	1	t
106104	416	12	43	6175	1	0	t
106124	416	13	13	6176	1	0	t
106073	416	12	12	6175	1	2	t
106075	416	12	14	6175	2	1	t
106076	416	12	15	6175	1	0	t
106175	416	14	14	6177	1	2	t
106204	416	14	43	6177	1	2	t
106126	416	13	15	6176	2	0	t
106127	416	13	16	6176	1	0	t
106128	416	13	17	6176	1	0	t
106077	416	12	16	6175	1	0	t
106179	416	14	18	6177	1	0	t
106178	416	14	17	6177	2	0	t
106180	416	14	19	6177	1	0	t
106129	416	13	18	6176	1	0	f
106181	416	14	20	6177	1	0	t
106080	416	12	19	6175	1	0	t
106132	416	13	21	6176	1	0	f
106081	416	12	20	6175	1	2	t
106055	416	11	44	6174	1	0	t
106133	416	13	22	6176	1	0	t
106182	416	14	21	6177	1	2	t
106184	416	14	23	6177	1	0	t
106183	416	14	22	6177	2	0	t
106056	416	11	45	6174	1	0	t
106185	416	14	24	6177	1	0	t
106084	416	12	23	6175	1	2	t
106136	416	13	25	6176	1	0	t
106085	416	12	24	6175	2	1	f
106155	416	13	44	6176	1	2	t
106086	416	12	25	6175	2	0	t
106106	416	12	45	6175	1	0	f
106157	416	13	46	6176	1	0	t
106206	416	14	45	6177	1	2	t
106158	416	13	47	6176	1	0	t
106057	416	11	46	6174	1	0	f
106107	416	12	46	6175	1	0	f
106109	416	12	48	6175	1	0	t
106058	416	11	47	6174	1	2	t
106059	416	11	48	6174	2	0	t
106060	416	11	49	6174	1	0	t
106110	416	12	49	6175	1	0	t
107120	417	3	9	6196	0	3	t
108322	417	27	11	6220	3	0	t
106237	416	15	26	6178	1	0	t
106238	416	15	27	6178	1	0	f
106337	416	17	26	6180	1	2	t
107872	417	18	11	6211	3	0	t
106338	416	17	27	6180	2	0	t
106288	416	16	27	6179	1	2	t
107972	417	20	11	6213	2	1	f
106239	416	15	28	6178	1	2	t
105790	416	6	29	6169	0	1	t
106139	416	13	28	6176	1	2	t
106290	416	16	29	6179	1	2	t
106291	416	16	30	6179	2	0	t
106341	416	17	30	6180	1	2	t
106292	416	16	31	6179	1	0	t
107094	417	2	33	6195	0	3	t
106242	416	15	31	6178	1	0	t
106243	416	15	32	6178	1	0	t
106342	416	17	31	6180	2	0	t
106244	416	15	33	6178	1	0	t
106293	416	16	32	6179	1	0	f
106245	416	15	34	6178	1	0	f
106344	416	17	33	6180	2	0	t
106346	416	17	35	6180	2	0	t
106345	416	17	34	6180	1	2	t
106247	416	15	36	6178	2	0	t
106246	416	15	35	6178	1	2	t
106296	416	16	35	6179	1	2	t
106248	416	15	37	6178	1	0	f
106347	416	17	36	6180	1	2	t
106348	416	17	37	6180	2	0	t
106249	416	15	38	6178	1	0	t
106350	416	17	39	6180	2	0	t
106349	416	17	38	6180	1	2	t
106251	416	15	40	6178	2	0	t
106250	416	15	39	6178	1	2	t
106300	416	16	39	6179	1	2	t
106252	416	15	41	6178	1	0	t
106351	416	17	40	6180	1	2	t
106253	416	15	42	6178	1	0	t
106352	416	17	41	6180	2	0	t
106353	416	17	42	6180	1	2	t
106354	416	17	43	6180	2	0	t
106254	416	15	43	6178	1	2	t
106261	416	16	0	6179	1	0	t
106255	416	15	44	6178	2	0	t
106213	416	15	2	6178	1	0	t
106214	416	15	3	6178	1	0	t
106363	416	18	2	6181	1	0	t
106263	416	16	2	6179	1	0	f
106265	416	16	4	6179	2	0	t
106217	416	15	6	6178	1	0	t
106315	416	17	4	6180	2	0	t
106215	416	15	4	6178	1	2	t
106266	416	16	5	6179	1	2	t
106316	416	17	5	6180	1	2	t
106304	416	16	43	6179	1	2	t
106267	416	16	6	6179	2	0	t
106218	416	15	7	6178	1	0	t
106219	416	15	8	6178	1	0	t
106268	416	16	7	6179	1	2	t
106220	416	15	9	6178	1	0	t
106269	416	16	8	6179	2	0	t
106221	416	15	10	6178	1	0	t
106270	416	16	9	6179	1	2	t
106271	416	16	10	6179	2	0	t
106272	416	16	11	6179	1	0	t
106256	416	15	45	6178	1	0	t
106222	416	15	11	6178	1	0	t
106273	416	16	12	6179	1	0	t
106223	416	15	12	6178	1	0	t
106224	416	15	13	6178	1	0	t
106355	416	17	44	6180	1	2	t
106274	416	16	13	6179	1	0	t
106275	416	16	14	6179	1	0	t
106225	416	15	14	6178	1	0	t
106226	416	15	15	6178	1	0	f
106227	416	15	16	6178	1	2	t
106276	416	16	15	6179	1	0	f
106228	416	15	17	6178	2	0	t
106277	416	16	16	6179	1	2	t
106229	416	15	18	6178	1	0	t
106278	416	16	17	6179	2	0	t
106230	416	15	19	6178	1	0	t
106279	416	16	18	6179	1	0	f
106231	416	15	20	6178	1	0	t
106257	416	15	46	6178	1	0	f
106232	416	15	21	6178	1	0	t
106281	416	16	20	6179	2	0	t
106306	416	16	45	6179	1	0	t
106332	416	17	21	6180	2	0	t
106233	416	15	22	6178	1	0	f
106334	416	17	23	6180	2	0	t
106333	416	17	22	6180	1	2	t
106284	416	16	23	6179	1	2	t
106285	416	16	24	6179	2	0	t
106236	416	15	25	6178	1	0	t
106335	416	17	24	6180	1	2	t
106307	416	16	46	6179	1	0	f
106336	416	17	25	6180	2	0	t
106258	416	15	47	6178	1	0	t
106259	416	15	48	6178	1	0	t
106358	416	17	47	6180	2	0	t
106210	416	14	49	6177	1	0	t
106359	416	17	48	6180	1	2	t
106310	416	16	49	6179	1	0	f
106260	416	15	49	6178	1	0	f
106360	416	17	49	6180	2	0	t
106487	416	20	26	6183	2	0	t
106488	416	20	27	6183	0	1	t
106387	416	18	26	6181	1	2	t
106489	416	20	28	6183	2	0	t
106438	416	19	27	6182	2	0	t
107770	417	16	9	6209	3	0	t
108622	417	33	11	6226	3	1	f
106389	416	18	28	6181	1	2	t
107772	417	16	11	6209	2	3	t
107794	417	16	33	6209	1	2	t
106490	416	20	29	6183	0	1	f
106491	416	20	30	6183	0	1	f
106390	416	18	29	6181	2	0	t
106492	416	20	31	6183	0	1	t
106391	416	18	30	6181	1	2	t
106442	416	19	31	6182	2	0	t
106493	416	20	32	6183	2	0	t
106392	416	18	31	6181	2	0	t
106494	416	20	33	6183	0	1	t
106443	416	19	32	6182	1	2	t
106495	416	20	34	6183	2	0	t
106394	416	18	33	6181	2	0	t
106444	416	19	33	6182	2	0	t
106395	416	18	34	6181	1	2	t
106496	416	20	35	6183	0	1	t
106396	416	18	35	6181	2	0	t
106497	416	20	36	6183	2	0	t
106498	416	20	37	6183	0	1	t
106397	416	18	36	6181	1	2	t
106499	416	20	38	6183	2	0	t
106398	416	18	37	6181	2	0	t
106448	416	19	37	6182	2	0	t
106399	416	18	38	6181	1	2	t
106500	416	20	39	6183	0	1	t
106501	416	20	40	6183	2	0	t
106400	416	18	39	6181	2	0	t
106502	416	20	41	6183	0	1	t
106401	416	18	40	6181	1	2	t
106503	416	20	42	6183	2	0	t
106402	416	18	41	6181	2	0	t
106452	416	19	41	6182	1	2	t
106504	416	20	43	6183	0	1	t
106403	416	18	42	6181	1	2	t
106454	416	19	43	6182	1	0	t
106455	416	19	44	6182	1	0	t
106506	416	20	45	6183	0	1	t
106364	416	18	3	6181	1	0	t
106512	416	21	1	6184	0	1	t
106505	416	20	44	6183	2	0	t
106413	416	19	2	6182	1	0	f
106414	416	19	3	6182	1	0	t
106465	416	20	4	6183	0	1	t
106365	416	18	4	6181	1	0	t
106366	416	18	5	6181	1	0	t
106466	416	20	5	6183	2	0	t
106467	416	20	6	6183	0	1	t
106507	416	20	46	6183	2	0	t
106368	416	18	7	6181	1	0	t
106367	416	18	6	6181	1	0	t
106517	416	21	6	6184	2	1	t
106406	416	18	45	6181	2	0	t
106468	416	20	7	6183	2	0	f
106369	416	18	8	6181	1	0	f
106469	416	20	8	6183	2	0	f
106370	416	18	9	6181	1	0	f
106419	416	19	8	6182	1	2	t
106471	416	20	10	6183	0	1	t
106470	416	20	9	6183	2	0	t
106420	416	19	9	6182	2	0	t
106422	416	19	11	6182	2	0	t
106371	416	18	10	6181	1	2	t
106456	416	19	45	6182	1	2	t
106372	416	18	11	6181	2	0	t
106423	416	19	12	6182	1	2	t
106373	416	18	12	6181	1	2	t
106474	416	20	13	6183	0	1	f
106475	416	20	14	6183	0	1	t
106374	416	18	13	6181	2	0	t
106476	416	20	15	6183	2	0	t
106375	416	18	14	6181	1	2	t
106376	416	18	15	6181	2	0	t
106477	416	20	16	6183	0	1	t
106478	416	20	17	6183	2	0	t
106377	416	18	16	6181	1	2	t
106407	416	18	46	6181	1	2	t
106479	416	20	18	6183	0	1	t
106378	416	18	17	6181	2	0	t
106480	416	20	19	6183	2	0	t
106379	416	18	18	6181	1	2	t
106508	416	20	47	6183	0	1	t
106380	416	18	19	6181	2	0	t
106481	416	20	20	6183	0	1	t
106482	416	20	21	6183	2	0	t
106381	416	18	20	6181	1	2	t
106483	416	20	22	6183	0	1	t
106382	416	18	21	6181	2	0	t
106484	416	20	23	6183	2	0	t
106383	416	18	22	6181	1	2	t
106459	416	19	48	6182	1	0	t
106384	416	18	23	6181	2	0	t
106485	416	20	24	6183	0	1	f
106486	416	20	25	6183	0	1	t
106385	416	18	24	6181	1	2	t
106458	416	19	47	6182	1	0	f
106386	416	18	25	6181	2	0	t
106509	416	20	48	6183	2	0	t
106510	416	20	49	6183	0	1	t
106410	416	18	49	6181	2	0	t
106460	416	19	49	6182	1	2	t
106637	416	23	26	6186	2	1	t
106587	416	22	26	6185	2	1	f
106538	416	21	27	6184	0	1	t
106588	416	22	27	6185	2	0	t
106589	416	22	28	6185	0	1	t
106638	416	23	27	6186	2	1	t
106540	416	21	29	6184	2	1	t
106539	416	21	28	6184	2	1	t
106641	416	23	30	6186	2	1	t
107270	417	6	9	6199	0	3	t
109672	417	54	11	6247	3	2	f
108772	417	36	11	6229	3	2	f
109073	417	42	12	6235	3	2	t
108424	417	29	13	6222	2	1	t
106640	416	23	29	6186	2	1	f
106541	416	21	30	6184	2	1	t
106592	416	22	31	6185	2	0	f
106593	416	22	32	6185	2	1	t
106542	416	21	31	6184	2	1	t
106642	416	23	31	6186	2	1	f
106644	416	23	33	6186	2	1	t
106543	416	21	32	6184	2	1	t
106544	416	21	33	6184	2	1	f
106546	416	21	35	6184	2	1	t
106645	416	23	34	6186	2	1	t
106545	416	21	34	6184	2	1	t
106596	416	22	35	6185	2	1	f
106547	416	21	36	6184	2	1	t
106646	416	23	35	6186	2	1	f
106597	416	22	36	6185	2	1	t
106598	416	22	37	6185	2	0	t
106599	416	22	38	6185	0	1	t
106648	416	23	37	6186	2	1	f
106600	416	22	39	6185	2	0	t
106649	416	23	38	6186	2	1	t
106601	416	22	40	6185	0	1	t
106650	416	23	39	6186	2	1	t
106550	416	21	39	6184	2	1	t
106552	416	21	41	6184	0	1	t
106651	416	23	40	6186	2	1	t
106602	416	22	41	6185	2	1	t
106603	416	22	42	6185	2	1	t
106604	416	22	43	6185	2	1	t
106553	416	21	42	6184	2	1	t
106555	416	21	44	6184	2	1	t
106554	416	21	43	6184	2	1	f
106654	416	23	43	6186	2	1	f
106612	416	23	1	6186	0	2	t
106663	416	24	2	6187	0	1	t
106563	416	22	2	6185	2	0	t
106664	416	24	3	6187	2	1	t
106615	416	23	4	6186	0	2	f
106605	416	22	44	6185	2	1	t
106665	416	24	4	6187	2	1	f
106616	416	23	5	6186	0	1	t
106666	416	24	5	6187	2	1	f
106667	416	24	6	6187	2	0	t
106668	416	24	7	6187	0	1	t
106617	416	23	6	6186	2	0	t
106567	416	22	6	6185	0	2	t
106619	416	23	8	6186	2	0	t
106656	416	23	45	6186	2	1	t
106569	416	22	8	6185	0	2	t
106620	416	23	9	6186	0	2	t
106570	416	22	9	6185	2	1	t
106671	416	24	10	6187	2	0	t
106672	416	24	11	6187	0	1	t
106621	416	23	10	6186	2	0	t
106573	416	22	12	6185	0	1	t
106622	416	23	11	6186	0	2	f
106556	416	21	45	6184	2	1	t
106623	416	23	12	6186	0	1	t
106673	416	24	12	6187	2	1	t
106574	416	22	13	6185	2	1	f
106575	416	22	14	6185	2	0	t
106624	416	23	13	6186	2	1	f
106576	416	22	15	6185	0	1	t
106675	416	24	14	6187	2	0	t
106525	416	21	14	6184	2	1	t
106625	416	23	14	6186	2	1	t
106627	416	23	16	6186	0	2	f
106526	416	21	15	6184	2	1	f
106657	416	23	46	6186	2	1	t
106527	416	21	16	6184	2	1	t
106628	416	23	17	6186	0	2	t
106528	416	21	17	6184	2	1	t
106529	416	21	18	6184	2	0	t
106608	416	22	47	6185	2	0	t
106629	416	23	18	6186	2	0	t
106630	416	23	19	6186	0	1	f
106530	416	21	19	6184	0	2	f
106531	416	21	20	6184	0	1	t
106557	416	21	46	6184	2	1	f
106631	416	23	20	6186	0	2	f
106632	416	23	21	6186	0	2	f
106532	416	21	21	6184	2	1	f
106633	416	23	22	6186	0	1	t
106584	416	22	23	6185	0	1	t
106533	416	21	22	6184	2	1	t
106635	416	23	24	6186	2	1	t
106634	416	23	23	6186	2	1	f
106586	416	22	25	6185	2	1	t
106585	416	22	24	6185	2	1	f
106609	416	22	48	6185	0	1	t
106636	416	23	25	6186	2	1	t
106658	416	23	47	6186	2	1	t
106660	416	23	49	6186	2	1	f
106659	416	23	48	6186	2	1	t
106610	416	22	49	6185	2	1	f
106687	416	24	26	6187	2	0	f
106688	416	24	27	6187	2	1	t
106787	416	26	26	6189	2	1	t
106689	416	24	28	6187	2	0	t
106788	416	26	27	6189	2	1	t
106690	416	24	29	6187	0	1	t
106739	416	25	28	6188	2	1	t
107670	417	14	9	6207	1	0	f
107773	417	16	12	6209	3	0	t
108274	417	26	13	6219	2	1	f
106789	416	26	28	6189	2	1	t
106740	416	25	29	6188	2	0	t
106741	416	25	30	6188	0	1	t
106691	416	24	30	6187	2	1	t
106692	416	24	31	6187	2	0	t
106693	416	24	32	6187	0	1	t
106742	416	25	31	6188	2	1	f
106793	416	26	32	6189	0	1	t
106743	416	25	32	6188	2	1	t
106794	416	26	33	6189	2	1	t
106745	416	25	34	6188	0	1	t
106694	416	24	33	6187	2	1	f
106795	416	26	34	6189	2	1	t
106697	416	24	36	6187	0	1	t
106796	416	26	35	6189	2	1	t
106746	416	25	35	6188	2	1	t
106797	416	26	36	6189	2	1	f
106798	416	26	37	6189	2	1	t
106747	416	25	36	6188	2	1	f
106749	416	25	38	6188	2	0	t
106698	416	24	37	6187	2	1	f
106750	416	25	39	6188	0	1	t
106799	416	26	38	6189	2	1	t
106801	416	26	40	6189	0	1	t
106800	416	26	39	6189	2	0	t
106701	416	24	40	6187	2	0	t
106702	416	24	41	6187	0	1	t
106751	416	25	40	6188	2	1	f
106802	416	26	41	6189	2	1	t
106703	416	24	42	6187	2	0	t
106754	416	25	43	6188	0	1	t
106753	416	25	42	6188	2	0	t
106704	416	24	43	6187	0	1	t
106705	416	24	44	6187	2	0	t
106805	416	26	44	6189	2	1	f
106706	416	24	45	6187	0	1	t
106755	416	25	44	6188	2	1	f
106712	416	25	1	6188	2	0	t
106713	416	25	2	6188	0	2	t
106813	416	27	2	6190	2	1	t
106714	416	25	3	6188	2	1	t
106715	416	25	4	6188	2	1	t
106707	416	24	46	6187	2	0	t
106816	416	27	5	6190	2	1	t
106815	416	27	4	6190	2	1	t
106716	416	25	5	6188	2	1	t
106817	416	27	6	6190	2	1	t
106806	416	26	45	6189	2	1	t
106717	416	25	6	6188	2	1	f
106718	416	25	7	6188	2	0	t
106719	416	25	8	6188	0	1	t
106818	416	27	7	6190	2	1	t
106769	416	26	8	6189	2	0	t
106770	416	26	9	6189	0	1	t
106721	416	25	10	6188	0	1	t
106720	416	25	9	6188	2	0	t
106771	416	26	10	6189	2	1	t
106772	416	26	11	6189	2	1	f
106722	416	25	11	6188	2	1	f
106723	416	25	12	6188	2	1	t
106724	416	25	13	6188	2	0	t
106773	416	26	12	6189	2	1	t
106725	416	25	14	6188	0	1	t
106775	416	26	14	6189	2	1	t
106676	416	24	15	6187	0	2	t
106757	416	25	46	6188	2	1	t
106776	416	26	15	6189	2	1	t
106677	416	24	16	6187	2	1	t
106728	416	25	17	6188	2	0	t
106777	416	26	16	6189	2	1	t
106827	416	27	16	6190	2	1	f
106778	416	26	17	6189	2	1	f
106729	416	25	18	6188	0	1	t
106678	416	24	17	6187	2	1	f
106708	416	24	47	6187	0	1	t
106779	416	26	18	6189	2	0	t
106780	416	26	19	6189	0	1	t
106680	416	24	19	6187	0	1	f
106681	416	24	20	6187	0	2	t
106730	416	25	19	6188	2	1	t
106781	416	26	20	6189	2	1	t
106731	416	25	20	6188	2	1	t
106782	416	26	21	6189	2	1	t
106683	416	24	22	6187	2	1	t
106682	416	24	21	6187	2	1	f
106733	416	25	22	6188	2	1	t
106734	416	25	23	6188	2	1	t
106684	416	24	23	6187	2	1	f
106685	416	24	24	6187	2	0	t
106759	416	25	48	6188	0	1	t
106686	416	24	25	6187	0	1	t
106785	416	26	24	6189	2	1	f
106758	416	25	47	6188	2	0	t
106786	416	26	25	6189	2	1	t
106709	416	24	48	6187	2	0	t
106710	416	24	49	6187	0	1	t
106760	416	25	49	6188	2	0	t
106810	416	26	49	6189	2	1	t
106837	416	27	26	6190	2	1	f
106938	416	29	27	6192	2	1	t
106937	416	29	26	6192	2	1	f
109620	417	53	9	6246	0	2	f
107073	417	2	12	6195	0	3	f
108074	417	22	13	6215	3	1	t
106888	416	28	27	6191	2	1	f
106939	416	29	28	6192	2	1	t
106439	416	19	28	6182	1	2	t
106889	416	28	28	6191	2	1	t
106440	416	19	29	6182	2	0	t
106840	416	27	29	6190	2	1	t
106940	416	29	29	6192	2	1	f
106841	416	27	30	6190	2	1	t
106942	416	29	31	6192	2	1	f
106943	416	29	32	6192	2	1	t
106892	416	28	31	6191	2	1	f
106893	416	28	32	6191	2	1	t
106944	416	29	33	6192	2	1	t
106895	416	28	34	6191	2	1	f
106894	416	28	33	6191	2	1	t
106844	416	27	33	6190	2	1	t
106945	416	29	34	6192	2	1	f
106846	416	27	35	6190	2	1	t
106898	416	28	37	6191	2	1	f
106946	416	29	35	6192	2	1	t
106947	416	29	36	6192	2	1	t
106847	416	27	36	6190	2	1	f
106948	416	29	37	6192	2	1	f
106949	416	29	38	6192	2	1	t
106848	416	27	37	6190	2	1	f
106950	416	29	39	6192	2	1	t
106899	416	28	38	6191	2	1	t
106901	416	28	40	6191	2	1	t
106900	416	28	39	6191	2	1	t
106951	416	29	40	6192	2	1	t
106111	416	13	0	6176	1	0	t
105561	416	2	0	6165	0	1	t
105661	416	4	0	6167	0	1	t
106952	416	29	41	6192	2	1	t
106161	416	14	0	6177	1	0	t
105911	416	9	0	6172	0	1	t
105761	416	6	0	6169	0	1	f
105861	416	8	0	6171	0	1	f
106953	416	29	42	6192	2	1	t
105862	416	8	1	6171	0	1	t
106262	416	16	1	6179	1	0	t
106162	416	14	1	6177	1	0	t
106913	416	29	2	6192	2	0	t
106914	416	29	3	6192	0	1	t
106863	416	28	2	6191	2	1	f
106915	416	29	4	6192	2	0	t
106864	416	28	3	6191	2	1	t
106916	416	29	5	6192	0	1	t
106865	416	28	4	6191	2	1	t
106917	416	29	6	6192	2	1	t
106866	416	28	5	6191	2	1	f
106918	416	29	7	6192	2	1	t
106867	416	28	6	6191	2	1	t
106869	416	28	8	6191	2	1	t
106868	416	28	7	6191	2	1	f
106919	416	29	8	6192	2	1	t
106920	416	29	9	6192	2	1	t
106871	416	28	10	6191	2	1	t
106870	416	28	9	6191	2	1	t
106921	416	29	10	6192	2	1	t
106922	416	29	11	6192	2	1	t
106923	416	29	12	6192	2	1	t
106872	416	28	11	6191	2	1	f
106874	416	28	13	6191	2	1	t
106873	416	28	12	6191	2	1	t
106924	416	29	13	6192	2	1	f
106925	416	29	14	6192	2	1	t
106876	416	28	15	6191	2	1	t
106875	416	28	14	6191	2	1	t
106877	416	28	16	6191	2	1	t
106926	416	29	15	6192	2	1	t
106928	416	29	17	6192	2	1	t
106929	416	29	18	6192	2	1	t
106878	416	28	17	6191	2	1	f
106930	416	29	19	6192	2	1	t
106852	416	27	41	6190	2	1	t
106931	416	29	20	6192	2	1	t
106882	416	28	21	6191	2	1	t
106834	416	27	23	6190	2	1	t
106832	416	27	21	6190	2	1	t
106902	416	28	41	6191	2	1	t
106883	416	28	22	6191	2	1	f
106934	416	29	23	6192	2	1	t
106835	416	27	24	6190	2	1	t
106935	416	29	24	6192	2	1	f
106936	416	29	25	6192	2	1	t
106904	416	28	43	6191	2	1	t
106836	416	27	25	6190	2	1	t
106853	416	27	42	6190	2	1	f
106854	416	27	43	6190	2	1	t
106905	416	28	44	6191	2	1	t
106906	416	28	45	6191	2	1	t
106855	416	27	44	6190	2	1	f
106857	416	27	46	6190	2	1	t
106856	416	27	45	6190	2	1	t
106958	416	29	47	6192	2	1	t
106907	416	28	46	6191	2	1	f
106959	416	29	48	6192	2	1	t
106858	416	27	47	6190	2	1	t
106859	416	27	48	6190	2	1	f
106860	416	27	49	6190	2	1	t
106960	416	29	49	6192	2	1	t
106910	416	28	49	6191	2	1	f
106511	416	21	0	6184	2	0	t
106611	416	23	0	6186	2	0	t
105711	416	5	0	6168	0	2	t
106339	416	17	28	6180	1	2	t
106561	416	22	0	6185	2	0	t
105461	416	0	0	6163	0	2	t
106461	416	20	0	6183	2	0	t
105811	416	7	0	6170	0	2	t
108944	417	39	33	6232	2	1	f
106911	416	29	0	6192	2	0	t
105611	416	3	0	6166	0	2	t
106340	416	17	29	6180	2	0	t
106661	416	24	0	6187	2	1	t
106061	416	12	0	6175	1	2	t
106890	416	28	29	6191	2	1	f
106711	416	25	0	6188	2	1	t
106361	416	18	0	6181	1	2	t
105691	416	4	30	6167	0	1	t
106761	416	26	0	6189	2	1	t
106011	416	11	0	6174	1	2	t
106091	416	12	30	6175	1	0	t
106811	416	27	0	6190	2	1	t
106211	416	15	0	6178	1	2	t
106241	416	15	30	6178	2	0	t
105491	416	0	30	6163	0	2	f
106861	416	28	0	6191	2	1	t
105961	416	10	0	6173	1	2	t
106441	416	19	30	6182	1	2	t
106311	416	17	0	6180	1	2	f
106092	416	12	31	6175	1	0	t
106411	416	19	0	6182	1	2	f
105462	416	0	1	6163	0	1	t
106462	416	20	1	6183	0	1	t
106412	416	19	1	6182	1	0	t
105712	416	5	1	6168	0	2	t
105962	416	10	1	6173	2	0	t
106362	416	18	1	6181	2	0	t
106912	416	29	1	6192	0	2	t
106012	416	11	1	6174	2	0	t
106562	416	22	1	6185	0	2	t
106662	416	24	1	6187	2	0	t
106212	416	15	1	6178	2	0	t
105812	416	7	1	6170	0	2	t
105612	416	3	1	6166	0	2	f
106862	416	28	1	6191	2	1	t
105562	416	2	1	6165	1	2	t
106762	416	26	1	6189	2	1	t
106062	416	12	1	6175	2	1	t
106312	416	17	1	6180	1	2	t
106812	416	27	1	6190	2	1	t
106313	416	17	2	6180	2	0	t
106463	416	20	2	6183	2	0	t
105713	416	5	2	6168	0	2	f
105763	416	6	2	6169	0	2	f
106613	416	23	2	6186	2	1	t
105963	416	10	2	6173	1	2	t
106513	416	21	2	6184	2	1	t
106163	416	14	2	6177	1	2	t
106763	416	26	2	6189	2	1	t
105764	416	6	3	6169	0	1	t
105464	416	0	3	6163	0	1	t
105714	416	5	3	6168	0	1	t
106464	416	20	3	6183	0	1	f
105914	416	9	3	6172	0	1	f
105814	416	7	3	6170	0	2	t
106614	416	23	3	6186	2	0	t
106564	416	22	3	6185	0	2	t
106114	416	13	3	6176	2	0	t
105614	416	3	3	6166	0	2	t
105964	416	10	3	6173	2	0	t
106514	416	21	3	6184	2	0	f
106764	416	26	3	6189	2	0	f
105564	416	2	3	6165	1	2	t
106264	416	16	3	6179	1	2	t
106814	416	27	3	6190	2	1	t
106314	416	17	3	6180	1	2	t
106164	416	14	3	6177	2	1	t
105565	416	2	4	6165	0	1	t
105715	416	5	4	6168	1	2	t
105765	416	6	4	6169	1	2	t
106515	416	21	4	6184	2	1	t
106015	416	11	4	6174	1	2	t
106065	416	12	4	6175	2	1	t
106415	416	19	4	6182	1	2	t
106765	416	26	4	6189	2	1	t
106565	416	22	4	6185	2	1	f
106066	416	12	5	6175	1	0	t
105766	416	6	5	6169	0	1	t
105716	416	5	5	6168	0	2	t
106566	416	22	5	6185	2	0	t
106416	416	19	5	6182	2	0	t
105566	416	2	5	6165	1	2	t
106216	416	15	5	6178	2	1	t
106016	416	11	5	6174	2	1	t
106766	416	26	5	6189	2	1	t
106516	416	21	5	6184	2	1	f
105967	416	10	6	6173	2	0	t
105467	416	0	6	6163	0	2	t
106317	416	17	6	6180	2	0	t
105717	416	5	6	6168	0	2	t
105767	416	6	6	6169	1	2	t
106167	416	14	6	6177	1	2	t
106417	416	19	6	6182	1	2	t
106767	416	26	6	6189	2	1	f
105718	416	5	7	6168	0	1	t
105968	416	10	7	6173	1	0	t
105768	416	6	7	6169	0	1	f
106418	416	19	7	6182	2	0	t
106568	416	22	7	6185	2	0	t
106618	416	23	7	6186	0	2	t
106168	416	14	7	6177	2	0	f
106768	416	26	7	6189	2	1	t
105469	416	0	8	6163	0	2	t
105568	416	2	7	6165	1	2	t
106518	416	21	7	6184	2	1	t
106318	416	17	7	6180	1	2	t
105969	416	10	8	6173	1	0	f
105869	416	8	8	6171	0	2	t
105490	416	0	29	6163	0	2	t
106319	416	17	8	6180	2	0	f
106819	416	27	8	6190	2	1	t
105541	416	1	30	6164	0	2	t
106669	416	24	8	6187	2	1	t
106891	416	28	30	6191	2	1	t
105669	416	4	8	6167	1	2	t
106519	416	21	8	6184	2	1	f
105991	416	10	30	6173	1	2	t
106169	416	14	8	6177	2	1	f
108320	417	27	9	6220	3	2	f
105670	416	4	9	6167	0	2	t
105870	416	8	9	6171	0	2	t
106320	416	17	9	6180	2	0	t
106170	416	14	9	6177	2	0	t
106791	416	26	30	6189	2	1	t
105970	416	10	9	6173	1	2	t
106520	416	21	9	6184	2	1	t
106820	416	27	9	6190	2	1	t
106670	416	24	9	6187	2	1	t
105571	416	2	10	6165	0	1	f
105471	416	0	10	6163	0	2	t
106521	416	21	10	6184	2	0	t
105771	416	6	10	6169	0	2	f
105792	416	6	31	6169	0	1	t
105721	416	5	10	6168	0	2	f
108744	417	35	33	6228	2	1	f
106021	416	11	10	6174	1	2	t
106321	416	17	10	6180	1	2	t
106071	416	12	10	6175	2	1	t
106421	416	19	10	6182	1	2	t
106821	416	27	10	6190	2	1	t
106571	416	22	10	6185	2	1	f
105772	416	6	11	6169	0	1	t
106072	416	12	11	6175	1	0	t
105722	416	5	11	6168	0	1	t
106572	416	22	11	6185	2	0	t
106022	416	11	11	6174	2	0	t
106322	416	17	11	6180	2	0	t
106522	416	21	11	6184	0	2	t
105572	416	2	11	6165	0	2	f
106472	416	20	11	6183	2	1	f
106822	416	27	11	6190	2	1	f
106473	416	20	12	6183	2	0	t
105673	416	4	12	6167	0	2	f
105923	416	9	12	6172	0	2	f
106523	416	21	12	6184	2	1	t
106323	416	17	12	6180	1	2	t
106173	416	14	12	6177	1	2	t
106823	416	27	12	6190	2	1	t
105823	416	7	12	6170	1	2	t
105624	416	3	13	6166	0	1	t
105924	416	9	13	6172	0	1	t
105974	416	10	13	6173	1	0	t
105774	416	6	13	6169	0	1	t
105474	416	0	13	6163	0	2	t
105824	416	7	13	6170	0	2	t
106174	416	14	13	6177	2	0	t
105674	416	4	13	6167	0	2	t
106324	416	17	13	6180	2	0	t
106424	416	19	13	6182	2	0	f
106524	416	21	13	6184	2	1	t
106774	416	26	13	6189	2	1	t
105574	416	2	13	6165	1	2	t
106074	416	12	13	6175	2	1	f
106674	416	24	13	6187	2	1	f
106824	416	27	13	6190	2	1	f
105475	416	0	14	6163	0	2	t
106425	416	19	14	6182	2	0	t
106325	416	17	14	6180	1	2	t
105625	416	3	14	6166	1	2	t
106825	416	27	14	6190	2	1	t
106125	416	13	14	6176	1	2	t
105925	416	9	14	6172	1	2	t
105875	416	8	14	6171	1	2	f
106176	416	14	15	6177	2	0	t
106626	416	23	15	6186	2	0	t
106326	416	17	15	6180	2	0	t
105676	416	4	15	6167	1	2	t
105876	416	8	15	6171	1	2	t
106826	416	27	15	6190	2	1	t
105976	416	10	15	6173	1	2	t
106426	416	19	15	6182	1	2	t
106726	416	25	15	6188	2	1	f
105977	416	10	16	6173	2	0	t
105577	416	2	16	6165	0	2	t
106427	416	19	16	6182	2	0	t
105877	416	8	16	6171	0	2	f
105677	416	4	16	6167	0	2	f
105477	416	0	16	6163	0	2	f
106727	416	25	16	6188	2	1	t
106577	416	22	16	6185	2	1	t
106327	416	17	16	6180	1	2	t
106177	416	14	16	6177	1	2	t
106927	416	29	16	6192	2	1	t
105878	416	8	17	6171	0	2	t
106328	416	17	17	6180	2	0	t
105678	416	4	17	6167	0	2	t
105928	416	9	17	6172	1	2	t
106078	416	12	17	6175	1	2	t
106428	416	19	17	6182	1	2	t
106578	416	22	17	6185	2	1	t
106828	416	27	17	6190	2	1	f
105679	416	4	18	6167	0	1	t
105879	416	8	18	6171	0	2	t
106429	416	19	18	6182	2	0	t
105480	416	0	19	6163	0	2	t
106280	416	16	19	6179	1	2	t
105929	416	9	18	6172	0	2	t
106679	416	24	18	6187	2	0	t
106079	416	12	18	6175	2	1	t
106329	416	17	18	6180	1	2	t
106579	416	22	18	6185	2	1	t
105687	416	4	26	6167	0	1	t
105579	416	2	18	6165	1	2	t
106879	416	28	18	6191	2	1	t
106829	416	27	18	6190	2	1	f
106287	416	16	26	6179	2	0	t
106537	416	21	26	6184	2	0	t
106330	416	17	19	6180	2	0	t
106187	416	14	26	6177	2	0	t
105880	416	8	19	6171	0	2	f
105487	416	0	26	6163	0	2	t
106580	416	22	19	6185	2	1	t
105987	416	10	26	6173	2	0	t
106430	416	19	19	6182	1	2	t
106437	416	19	26	6182	2	0	f
106880	416	28	19	6191	2	1	t
105680	416	4	19	6167	1	2	t
106887	416	28	26	6191	2	1	t
105887	416	8	26	6171	1	2	t
106830	416	27	19	6190	2	1	t
105980	416	10	19	6173	1	2	t
105940	416	9	29	6172	0	2	f
106130	416	13	19	6176	1	2	f
106131	416	13	20	6176	1	0	t
105581	416	2	20	6165	0	1	f
105681	416	4	20	6167	0	1	f
105981	416	10	20	6173	2	0	t
106431	416	19	20	6182	2	0	t
105881	416	8	20	6171	0	2	t
105481	416	0	20	6163	0	2	f
106581	416	22	20	6185	2	1	t
106881	416	28	20	6191	2	1	t
106331	416	17	20	6180	1	2	t
106831	416	27	20	6190	2	1	f
105932	416	9	21	6172	0	1	t
106591	416	22	30	6185	2	1	f
105682	416	4	21	6167	0	2	f
106941	416	29	30	6192	2	1	f
105482	416	0	21	6163	0	2	f
105832	416	7	21	6170	1	2	t
106732	416	25	21	6188	2	1	t
105492	416	0	31	6163	0	2	t
106282	416	16	21	6179	1	2	t
107520	417	11	9	6204	1	0	t
106432	416	19	21	6182	1	2	t
106792	416	26	31	6189	2	0	t
107373	417	8	12	6201	0	3	f
106932	416	29	21	6192	2	1	f
106582	416	22	21	6185	2	1	f
105992	416	10	31	6173	2	1	t
106082	416	12	21	6175	2	1	f
108423	417	29	12	6222	2	1	t
106433	416	19	22	6182	2	0	t
106283	416	16	22	6179	2	0	t
106583	416	22	22	6185	2	0	t
105483	416	0	22	6163	0	2	t
105833	416	7	22	6170	0	2	f
105683	416	4	22	6167	0	2	f
106842	416	27	31	6190	2	1	f
106933	416	29	22	6192	2	1	t
106783	416	26	22	6189	2	1	t
106083	416	12	22	6175	2	1	t
105933	416	9	22	6172	1	2	t
106833	416	27	22	6190	2	1	f
105984	416	10	23	6173	2	0	t
105584	416	2	23	6165	0	2	t
105484	416	0	23	6163	0	2	t
105834	416	7	23	6170	0	2	f
105684	416	4	23	6167	0	2	f
106134	416	13	23	6176	1	2	t
106784	416	26	23	6189	2	1	t
106234	416	15	23	6178	1	2	t
106884	416	28	23	6191	2	1	t
106434	416	19	23	6182	1	2	t
105693	416	4	32	6167	0	1	t
106534	416	21	23	6184	2	1	f
105843	416	7	32	6170	0	2	f
105835	416	7	24	6170	0	1	t
105985	416	10	24	6173	1	0	t
105685	416	4	24	6167	0	1	t
105535	416	1	24	6164	0	2	t
106343	416	17	32	6180	1	2	t
106435	416	19	24	6182	2	0	t
106235	416	15	24	6178	2	0	t
106135	416	13	24	6176	2	0	t
106885	416	28	24	6191	2	1	t
106535	416	21	24	6184	2	1	f
106735	416	25	24	6188	2	1	f
105886	416	8	25	6171	0	1	t
106643	416	23	32	6186	2	1	t
105736	416	5	25	6168	0	2	t
105486	416	0	25	6163	0	2	t
106393	416	18	32	6181	1	2	t
105686	416	4	25	6167	1	2	t
106843	416	27	32	6190	2	1	t
105986	416	10	25	6173	1	2	t
106186	416	14	25	6177	1	2	t
106736	416	25	25	6188	2	1	t
106286	416	16	25	6179	1	2	t
106436	416	19	25	6182	1	2	t
106886	416	28	25	6191	2	1	f
106536	416	21	25	6184	2	1	f
105944	416	9	33	6172	0	1	f
105494	416	0	33	6163	0	2	t
106744	416	25	33	6188	2	0	t
106144	416	13	33	6176	2	0	t
105694	416	4	33	6167	1	2	t
105695	416	4	34	6167	0	1	t
105545	416	1	34	6164	0	2	f
106445	416	19	34	6182	1	2	t
106294	416	16	33	6179	1	2	t
105894	416	8	33	6171	1	2	t
108570	417	32	9	6225	3	1	t
106594	416	22	33	6185	2	1	f
108993	417	40	32	6233	3	1	f
105895	416	8	34	6171	0	2	t
108844	417	37	33	6230	2	1	f
106295	416	16	34	6179	2	0	t
105945	416	9	34	6172	0	2	f
106195	416	14	34	6177	1	2	t
106595	416	22	34	6185	2	1	t
107444	417	9	33	6202	1	3	t
106695	416	24	34	6187	2	1	t
108294	417	26	33	6219	3	1	t
106845	416	27	34	6190	2	1	f
105946	416	9	35	6172	0	1	t
106446	416	19	35	6182	2	0	t
106196	416	14	35	6177	2	0	t
106696	416	24	35	6187	2	0	t
105896	416	8	35	6171	0	2	f
109524	417	51	13	6244	3	0	t
106896	416	28	35	6191	2	1	f
105697	416	4	36	6167	0	1	f
105497	416	0	36	6163	0	2	t
105547	416	1	36	6164	0	2	t
106297	416	16	36	6179	2	0	t
105747	416	5	36	6168	0	2	f
105947	416	9	36	6172	1	2	t
106897	416	28	36	6191	2	1	t
106647	416	23	36	6186	2	1	t
106447	416	19	36	6182	1	2	t
105548	416	1	37	6164	0	2	t
105898	416	8	37	6171	0	2	t
105698	416	4	37	6167	0	2	t
106198	416	14	37	6177	2	0	t
105948	416	9	37	6172	0	2	f
105798	416	6	37	6169	1	2	t
106298	416	16	37	6179	1	2	t
106748	416	25	37	6188	2	1	t
106548	416	21	37	6184	2	1	f
105699	416	4	38	6167	0	2	t
106299	416	16	38	6179	2	0	t
106549	416	21	38	6184	2	1	t
105999	416	10	38	6173	1	2	t
106199	416	14	38	6177	1	2	t
106849	416	27	38	6190	2	1	t
106449	416	19	38	6182	1	2	t
106699	416	24	38	6187	2	1	f
106200	416	14	39	6177	2	0	t
106000	416	10	39	6173	2	0	t
105850	416	7	39	6170	0	2	t
105550	416	1	39	6164	0	2	t
106450	416	19	39	6182	2	0	f
106850	416	27	39	6190	2	1	t
106700	416	24	39	6187	2	1	f
106151	416	13	40	6176	2	0	t
105701	416	4	40	6167	0	2	t
105501	416	0	40	6163	0	2	t
106451	416	19	40	6182	2	0	t
106551	416	21	40	6184	2	0	t
105751	416	5	40	6168	0	2	t
106301	416	16	40	6179	2	0	t
106851	416	27	40	6190	2	1	f
105752	416	5	41	6168	0	2	f
105652	416	3	41	6166	0	2	f
105952	416	9	41	6172	0	2	f
106302	416	16	41	6179	1	2	t
106152	416	13	41	6176	1	2	t
106752	416	25	41	6188	2	1	f
106652	416	23	41	6186	2	1	f
105653	416	3	42	6166	0	2	t
106303	416	16	42	6179	2	0	t
105553	416	1	42	6164	0	2	t
106153	416	13	42	6176	2	0	t
106453	416	19	42	6182	2	0	t
106653	416	23	42	6186	2	1	f
106903	416	28	42	6191	2	1	f
106803	416	26	42	6189	2	1	f
105854	416	7	43	6170	0	1	t
106404	416	18	43	6181	2	0	t
106054	416	11	43	6174	2	0	t
105554	416	1	43	6164	0	2	f
106954	416	29	43	6192	2	1	t
106804	416	26	43	6189	2	1	t
105955	416	9	44	6172	0	1	t
106305	416	16	44	6179	2	0	t
105505	416	0	44	6163	0	2	t
106205	416	14	44	6177	2	0	t
105655	416	3	44	6166	0	2	f
105855	416	7	44	6170	1	2	t
106655	416	23	44	6186	2	1	t
106955	416	29	44	6192	2	1	t
106405	416	18	44	6181	1	2	t
105856	416	7	45	6170	0	1	t
106356	416	17	45	6180	2	0	t
105556	416	1	45	6164	0	2	t
106156	416	13	45	6176	2	0	t
105606	416	2	45	6165	0	2	f
105956	416	9	45	6172	1	2	t
106606	416	22	45	6185	2	1	f
106956	416	29	45	6192	2	1	f
106756	416	25	45	6188	2	1	f
105957	416	9	46	6172	0	1	t
106207	416	14	46	6177	2	0	t
106457	416	19	46	6182	2	0	t
105607	416	2	46	6165	0	2	f
105857	416	7	46	6170	1	2	t
106357	416	17	46	6180	1	2	t
106607	416	22	46	6185	2	1	f
105858	416	7	47	6170	0	1	t
106108	416	12	47	6175	1	0	t
106957	416	29	46	6192	2	1	f
106807	416	26	46	6189	2	1	f
106969	417	0	8	6193	0	2	f
106408	416	18	47	6181	2	0	t
106973	417	0	12	6193	0	1	t
107019	417	1	8	6194	0	3	t
105608	416	2	47	6165	0	2	f
106558	416	21	47	6184	2	1	t
105958	416	9	47	6172	1	2	t
106908	416	28	47	6191	2	1	t
106308	416	16	47	6179	1	2	t
106970	417	0	9	6193	0	1	t
106808	416	26	47	6189	2	1	t
106208	416	14	47	6177	1	2	t
106971	417	0	10	6193	1	3	t
105559	416	1	48	6164	0	2	t
105959	416	9	48	6172	0	2	t
106209	416	14	48	6177	2	0	t
106309	416	16	48	6179	2	0	t
105509	416	0	48	6163	0	2	t
105709	416	4	48	6167	0	2	f
107020	417	1	9	6194	0	3	t
105859	416	7	48	6170	1	2	t
107870	417	18	9	6211	3	2	f
106159	416	13	48	6176	1	2	t
106559	416	21	48	6184	2	1	t
106409	416	18	48	6181	1	2	t
106809	416	26	48	6189	2	1	t
106909	416	28	48	6191	2	1	f
105860	416	7	49	6170	0	1	t
106160	416	13	49	6176	2	0	t
105710	416	4	49	6167	0	2	t
105560	416	1	49	6164	0	2	f
105960	416	9	49	6172	0	2	f
105810	416	6	49	6169	1	2	t
106010	416	10	49	6173	1	2	t
106560	416	21	49	6184	2	1	f
107021	417	1	10	6194	0	3	t
106972	417	0	11	6193	0	3	t
107022	417	1	11	6194	0	3	t
107023	417	1	12	6194	0	3	f
106992	417	0	31	6193	1	3	t
107593	417	12	32	6205	1	0	t
107594	417	12	33	6205	1	0	f
106995	417	0	34	6193	0	1	t
107046	417	1	35	6194	0	3	t
107045	417	1	34	6194	0	3	f
106996	417	0	35	6193	1	3	t
106997	417	0	36	6193	0	2	f
106998	417	0	37	6193	0	3	t
106999	417	0	38	6193	0	1	t
107000	417	0	39	6193	1	3	t
107001	417	0	40	6193	0	2	t
109223	417	45	12	6238	3	2	f
107002	417	0	41	6193	2	3	t
107003	417	0	42	6193	0	1	t
107004	417	0	43	6193	1	3	t
107006	417	0	45	6193	0	2	f
107007	417	0	46	6193	0	1	f
107008	417	0	47	6193	0	1	t
107010	417	0	49	6193	0	3	f
106961	417	0	0	6193	0	1	t
107011	417	1	0	6194	0	3	t
107012	417	1	1	6194	0	3	t
106962	417	0	1	6193	1	3	t
106963	417	0	2	6193	0	2	t
107013	417	1	2	6194	0	3	t
107014	417	1	3	6194	0	3	t
107016	417	1	5	6194	0	3	f
106964	417	0	3	6193	2	3	t
106965	417	0	4	6193	0	3	t
107015	417	1	4	6194	0	3	t
106966	417	0	5	6193	0	3	t
107017	417	1	6	6194	0	3	t
106967	417	0	6	6193	0	1	t
106968	417	0	7	6193	1	3	t
107018	417	1	7	6194	0	3	t
109024	417	41	13	6234	3	0	t
109224	417	45	13	6238	3	0	t
108874	417	38	13	6231	3	0	t
107024	417	1	13	6194	0	3	t
107025	417	1	14	6194	0	3	t
106974	417	0	13	6193	1	3	t
106976	417	0	15	6193	0	1	t
107027	417	1	16	6194	0	3	t
107026	417	1	15	6194	0	3	t
106977	417	0	16	6193	1	3	t
106978	417	0	17	6193	0	2	t
107029	417	1	18	6194	0	3	t
107028	417	1	17	6194	0	3	t
106979	417	0	18	6193	2	3	t
106980	417	0	19	6193	0	3	t
107031	417	1	20	6194	0	3	t
107030	417	1	19	6194	0	3	f
106981	417	0	20	6193	0	3	f
106982	417	0	21	6193	0	1	t
107032	417	1	21	6194	0	3	t
107033	417	1	22	6194	0	3	t
106983	417	0	22	6193	1	3	t
107034	417	1	23	6194	0	3	t
107036	417	1	25	6194	0	3	t
106984	417	0	23	6193	0	3	f
107035	417	1	24	6194	0	3	t
106987	417	0	26	6193	0	1	t
107037	417	1	26	6194	0	3	t
106988	417	0	27	6193	1	3	t
106989	417	0	28	6193	0	2	t
106990	417	0	29	6193	2	3	t
106991	417	0	30	6193	0	1	t
107041	417	1	30	6194	0	3	t
107169	417	4	8	6197	0	1	t
107069	417	2	8	6195	0	3	f
107192	417	4	31	6197	0	2	t
107071	417	2	10	6195	0	1	t
107070	417	2	9	6195	0	3	f
107170	417	4	9	6197	1	3	t
107092	417	2	31	6195	0	3	t
107443	417	9	32	6202	0	1	t
108893	417	38	32	6231	2	0	t
106993	417	0	32	6193	0	2	t
107793	417	16	32	6209	3	0	t
107195	417	4	34	6197	0	1	t
106994	417	0	33	6193	2	3	t
107095	417	2	34	6195	0	3	t
107096	417	2	35	6195	0	3	t
107196	417	4	35	6197	1	3	t
107172	417	4	11	6197	0	1	t
107121	417	3	10	6196	0	3	f
107122	417	3	11	6196	0	3	t
107124	417	3	13	6196	0	3	t
107097	417	2	36	6195	0	3	t
107048	417	1	37	6194	0	3	t
107047	417	1	36	6194	0	3	t
107199	417	4	38	6197	0	1	t
107198	417	4	37	6197	0	3	f
107098	417	2	37	6195	0	3	f
107149	417	3	38	6196	0	3	t
107049	417	1	38	6194	0	3	t
107150	417	3	39	6196	0	3	f
107100	417	2	39	6195	0	3	f
107200	417	4	39	6197	1	3	t
107072	417	2	11	6195	1	3	t
107123	417	3	12	6196	0	3	f
107173	417	4	12	6197	1	3	t
107151	417	3	40	6196	0	3	t
107101	417	2	40	6195	0	3	t
107152	417	3	41	6196	0	3	f
107051	417	1	40	6194	0	3	t
107102	417	2	41	6195	0	3	f
107053	417	1	42	6194	0	3	t
107202	417	4	41	6197	2	3	t
107103	417	2	42	6195	0	3	t
107104	417	2	43	6195	0	3	t
107153	417	3	42	6196	0	3	t
107105	417	2	44	6195	0	3	t
107054	417	1	43	6194	0	3	t
107106	417	2	45	6195	0	3	t
107055	417	1	44	6194	0	3	f
107174	417	4	13	6197	0	3	t
107113	417	3	2	6196	0	3	t
107112	417	3	1	6196	0	3	t
107076	417	2	15	6195	0	3	t
107163	417	4	2	6197	1	3	t
107114	417	3	3	6196	0	3	t
107065	417	2	4	6195	0	3	t
107125	417	3	14	6196	0	3	t
107115	417	3	4	6196	0	3	f
107116	417	3	5	6196	0	3	t
107066	417	2	5	6195	0	3	t
107167	417	4	6	6197	0	2	f
107067	417	2	6	6195	0	3	t
107168	417	4	7	6197	0	3	t
107068	417	2	7	6195	0	3	t
107155	417	3	44	6196	0	3	f
107126	417	3	15	6196	0	3	t
107176	417	4	15	6197	2	3	t
107127	417	3	16	6196	0	3	t
107078	417	2	17	6195	0	3	t
107077	417	2	16	6195	0	3	f
107079	417	2	18	6195	0	3	t
107128	417	3	17	6196	0	3	t
107180	417	4	19	6197	0	1	t
107107	417	2	46	6195	0	3	t
107129	417	3	18	6196	0	3	f
107130	417	3	19	6196	0	3	t
107131	417	3	20	6196	0	3	f
107181	417	4	20	6197	1	3	t
107182	417	4	21	6197	0	2	t
107056	417	1	45	6194	0	3	t
107082	417	2	21	6195	0	3	t
107083	417	2	22	6195	0	3	t
107184	417	4	23	6197	0	3	t
107183	417	4	22	6197	2	3	t
107084	417	2	23	6195	0	3	f
107185	417	4	24	6197	0	1	t
107085	417	2	24	6195	0	3	t
107086	417	2	25	6195	0	3	t
107137	417	3	26	6196	0	3	t
107136	417	3	25	6196	0	3	t
107087	417	2	26	6195	0	3	t
107188	417	4	27	6197	0	1	f
107190	417	4	29	6197	0	1	t
107138	417	3	27	6196	0	3	t
107139	417	3	28	6196	0	3	f
107189	417	4	28	6197	0	3	f
107108	417	2	47	6195	0	3	t
107090	417	2	29	6195	0	3	t
107091	417	2	30	6195	0	3	t
107157	417	3	46	6196	0	3	f
107191	417	4	30	6197	1	3	t
107158	417	3	47	6196	0	3	t
107159	417	3	48	6196	0	3	t
107109	417	2	48	6195	0	3	f
107110	417	2	49	6195	0	3	f
107160	417	3	49	6196	0	3	f
107319	417	7	8	6200	0	3	t
107220	417	5	9	6198	0	2	t
107219	417	5	8	6198	0	3	f
107320	417	7	9	6200	0	3	f
107342	417	7	31	6200	0	3	t
107242	417	5	31	6198	0	3	f
107143	417	3	32	6196	0	3	t
109093	417	42	32	6235	3	0	t
107043	417	1	32	6194	0	3	t
107295	417	6	34	6199	0	3	t
107144	417	3	33	6196	0	3	f
107245	417	5	34	6198	0	3	f
107246	417	5	35	6198	0	3	t
107345	417	7	34	6200	0	3	f
107296	417	6	35	6199	0	3	t
107297	417	6	36	6199	0	3	t
107271	417	6	10	6199	0	2	f
107321	417	7	10	6200	0	2	f
107223	417	5	12	6198	0	3	t
107322	417	7	11	6200	0	3	t
107272	417	6	11	6199	0	3	t
107247	417	5	36	6198	0	3	t
107298	417	6	37	6199	0	3	t
107349	417	7	38	6200	0	3	f
107248	417	5	37	6198	0	3	t
107299	417	6	38	6199	0	3	f
107350	417	7	39	6200	0	3	t
107249	417	5	38	6198	0	3	f
107300	417	6	39	6199	0	3	t
107251	417	5	40	6198	0	3	t
107252	417	5	41	6198	0	3	t
107351	417	7	40	6200	0	3	t
107225	417	5	14	6198	0	3	t
107273	417	6	12	6199	0	3	f
107323	417	7	12	6200	0	3	f
107274	417	6	13	6199	0	2	t
107352	417	7	41	6200	0	3	f
107203	417	4	42	6197	0	3	t
107353	417	7	42	6200	0	3	f
107204	417	4	43	6197	0	1	t
107354	417	7	43	6200	0	3	t
107355	417	7	44	6200	0	3	t
107254	417	5	43	6198	0	3	t
107255	417	5	44	6198	0	3	t
107307	417	6	46	6199	0	3	t
107305	417	6	44	6199	0	3	t
107224	417	5	13	6198	0	3	t
107312	417	7	1	6200	0	3	t
107313	417	7	2	6200	0	3	t
107263	417	6	2	6199	1	3	t
107314	417	7	3	6200	0	3	t
107215	417	5	4	6198	0	1	t
107265	417	6	4	6199	0	2	t
107317	417	7	6	6200	0	2	t
107216	417	5	5	6198	1	3	t
107266	417	6	5	6199	2	3	t
107325	417	7	14	6200	1	3	t
107217	417	5	6	6198	0	3	t
107218	417	5	7	6198	0	3	t
107318	417	7	7	6200	2	3	t
107226	417	5	15	6198	0	3	t
107326	417	7	15	6200	0	3	f
107227	417	5	16	6198	0	3	t
107256	417	5	45	6198	0	3	t
107328	417	7	17	6200	0	2	f
107327	417	7	16	6200	0	3	f
107228	417	5	17	6198	0	3	t
107279	417	6	18	6199	0	1	t
107229	417	5	18	6198	0	3	t
107230	417	5	19	6198	0	3	t
107231	417	5	20	6198	0	3	t
107280	417	6	19	6199	1	3	t
107356	417	7	45	6200	0	3	t
107282	417	6	21	6199	0	2	f
107281	417	6	20	6199	0	3	t
107232	417	5	21	6198	0	3	t
107333	417	7	22	6200	0	3	t
107334	417	7	23	6200	0	3	t
107233	417	5	22	6198	0	3	t
107234	417	5	23	6198	0	3	f
107335	417	7	24	6200	0	3	t
107306	417	6	45	6199	0	3	t
107235	417	5	24	6198	0	3	t
107236	417	5	25	6198	0	3	t
107336	417	7	25	6200	0	3	t
107287	417	6	26	6199	0	2	f
107237	417	5	26	6198	0	3	t
107288	417	6	27	6199	0	3	t
107238	417	5	27	6198	0	3	f
107289	417	6	28	6199	0	1	t
107339	417	7	28	6200	0	3	t
107341	417	7	30	6200	0	3	t
107340	417	7	29	6200	0	3	t
107290	417	6	29	6199	1	3	t
107357	417	7	46	6200	0	3	t
107241	417	5	30	6198	0	3	t
107207	417	4	46	6197	0	3	t
107308	417	6	47	6199	0	3	t
107358	417	7	47	6200	0	3	t
107309	417	6	48	6199	0	3	t
107259	417	5	48	6198	0	3	t
107210	417	4	49	6197	0	2	f
107209	417	4	48	6197	1	3	t
107310	417	6	49	6199	0	3	t
107260	417	5	49	6198	0	3	f
107469	417	10	8	6203	3	0	t
107370	417	8	9	6201	0	3	t
107369	417	8	8	6201	0	3	f
107492	417	10	31	6203	1	0	t
107420	417	9	9	6202	0	3	f
107493	417	10	32	6203	1	0	t
107392	417	8	31	6201	0	3	t
107494	417	10	33	6203	1	0	t
107093	417	2	32	6195	0	3	t
107495	417	10	34	6203	1	0	t
107044	417	1	33	6194	0	3	t
107496	417	10	35	6203	1	0	t
107395	417	8	34	6201	0	3	f
107497	417	10	36	6203	1	0	t
107396	417	8	35	6201	0	1	t
107446	417	9	35	6202	0	2	f
107470	417	10	9	6203	1	2	t
107371	417	8	10	6201	0	3	t
107422	417	9	11	6202	0	1	t
107421	417	9	10	6202	0	3	f
107498	417	10	37	6203	1	0	t
107397	417	8	36	6201	1	3	t
107499	417	10	38	6203	1	0	t
107448	417	9	37	6202	0	1	t
107500	417	10	39	6203	1	0	f
107449	417	9	38	6202	1	3	t
107401	417	8	40	6201	0	3	t
107400	417	8	39	6201	0	3	t
107450	417	9	39	6202	0	3	t
107501	417	10	40	6203	1	2	t
107452	417	9	41	6202	0	1	t
107472	417	10	11	6203	1	0	f
107473	417	10	12	6203	1	2	t
107423	417	9	12	6202	1	3	t
107474	417	10	13	6203	2	0	t
107502	417	10	41	6203	2	0	t
107503	417	10	42	6203	1	0	t
107504	417	10	43	6203	1	0	t
107453	417	9	42	6202	1	3	t
107404	417	8	43	6201	0	3	t
107505	417	10	44	6203	1	0	f
107454	417	9	43	6202	0	3	t
107456	417	9	45	6202	0	1	t
107405	417	8	44	6201	0	3	t
107508	417	10	47	6203	1	0	t
107406	417	8	45	6201	0	3	t
107424	417	9	13	6202	0	2	t
107374	417	8	13	6201	0	3	t
107475	417	10	14	6203	1	2	t
107461	417	10	0	6203	1	0	f
107463	417	10	2	6203	2	0	t
107425	417	9	14	6202	2	3	t
107363	417	8	2	6201	0	3	t
107364	417	8	3	6201	0	3	f
107464	417	10	3	6203	1	3	t
107415	417	9	4	6202	0	1	t
107366	417	8	5	6201	0	1	t
107365	417	8	4	6201	0	2	f
107476	417	10	15	6203	2	0	t
107465	417	10	4	6203	3	0	t
107466	417	10	5	6203	1	2	t
107407	417	8	46	6201	0	3	f
107367	417	8	6	6201	1	0	t
107467	417	10	6	6203	2	0	t
107376	417	8	15	6201	0	3	f
107368	417	8	7	6201	0	3	f
107468	417	10	7	6203	1	3	t
107377	417	8	16	6201	0	3	f
107477	417	10	16	6203	1	3	t
107378	417	8	17	6201	0	2	t
107429	417	9	18	6202	0	2	t
107428	417	9	17	6202	0	3	t
107480	417	10	19	6203	1	0	t
107379	417	8	18	6201	2	3	t
107457	417	9	46	6202	1	3	t
107380	417	8	19	6201	0	3	t
107481	417	10	20	6203	1	0	f
107382	417	8	21	6201	0	3	t
107381	417	8	20	6201	0	3	f
107482	417	10	21	6203	1	2	t
107483	417	10	22	6203	2	0	t
107384	417	8	23	6201	0	3	f
107383	417	8	22	6201	0	3	f
107484	417	10	23	6203	1	2	t
107385	417	8	24	6201	0	1	t
107485	417	10	24	6203	2	0	f
107436	417	9	25	6202	0	1	f
107509	417	10	48	6203	1	0	t
107486	417	10	25	6203	2	1	f
107487	417	10	26	6203	2	0	t
107438	417	9	27	6202	0	2	f
107437	417	9	26	6202	0	3	t
107439	417	9	28	6202	0	3	t
107388	417	8	27	6201	0	3	t
107389	417	8	28	6201	0	3	t
107440	417	9	29	6202	0	2	t
107458	417	9	47	6202	0	3	t
107391	417	8	30	6201	0	3	t
107390	417	8	29	6201	0	3	t
107441	417	9	30	6202	2	3	t
107510	417	10	49	6203	1	0	t
107459	417	9	48	6202	0	3	t
107359	417	7	48	6200	0	3	t
107460	417	9	49	6202	0	3	f
107360	417	7	49	6200	0	3	f
107569	417	12	8	6205	1	0	t
107619	417	13	8	6206	1	0	t
107519	417	11	8	6204	1	0	t
107642	417	13	31	6206	1	0	t
107543	417	11	32	6204	1	0	t
107592	417	12	31	6205	1	0	t
107643	417	13	32	6206	1	0	t
107644	417	13	33	6206	1	0	f
107544	417	11	33	6204	1	0	f
107645	417	13	34	6206	1	0	t
107646	417	13	35	6206	1	0	t
107595	417	12	34	6205	1	0	t
107545	417	11	34	6204	1	2	t
107596	417	12	35	6205	1	0	t
107570	417	12	9	6205	1	0	t
107647	417	13	36	6206	1	0	t
107620	417	13	9	6206	1	0	f
107571	417	12	10	6205	1	0	t
107648	417	13	37	6206	1	0	t
108720	417	35	9	6228	3	1	t
107547	417	11	36	6204	1	0	t
107548	417	11	37	6204	1	0	t
107549	417	11	38	6204	1	0	t
107651	417	13	40	6206	1	0	t
107599	417	12	38	6205	1	0	t
107649	417	13	38	6206	1	0	f
107550	417	11	39	6204	1	0	t
107600	417	12	39	6205	1	0	f
107551	417	11	40	6204	1	0	t
107652	417	13	41	6206	1	0	t
107603	417	12	42	6205	1	0	t
107552	417	11	41	6204	1	0	f
107521	417	11	10	6204	1	0	t
107623	417	13	12	6206	1	0	t
107572	417	12	11	6205	1	0	f
107653	417	13	42	6206	1	0	f
107604	417	12	43	6205	1	0	t
107553	417	11	42	6204	1	2	t
107654	417	13	43	6206	1	0	f
107605	417	12	44	6205	1	0	f
107655	417	13	44	6206	1	0	f
107606	417	12	45	6205	1	0	t
107656	417	13	45	6206	1	0	f
107557	417	11	46	6204	1	0	t
107558	417	11	47	6204	1	0	t
107657	417	13	46	6206	1	0	t
107573	417	12	12	6205	1	0	t
107523	417	11	12	6204	1	2	t
107574	417	12	13	6205	1	0	t
107624	417	13	13	6206	1	0	t
107524	417	11	13	6204	2	0	t
107625	417	13	14	6206	1	0	t
107662	417	14	1	6207	1	0	t
107663	417	14	2	6207	1	0	t
107664	417	14	3	6207	1	0	t
107613	417	13	2	6206	2	0	t
107525	417	11	14	6204	1	0	t
107615	417	13	4	6206	1	0	t
107526	417	11	15	6204	1	0	t
107616	417	13	5	6206	1	0	t
107665	417	14	4	6207	1	0	t
107617	417	13	6	6206	1	0	t
107575	417	12	14	6205	1	0	t
107667	417	14	6	6207	1	0	t
107518	417	11	7	6204	1	0	t
107517	417	11	6	6204	2	0	t
107668	417	14	7	6207	1	0	t
107618	417	13	7	6206	1	0	t
107607	417	12	46	6205	1	0	t
107626	417	13	15	6206	1	0	t
107559	417	11	48	6204	1	0	f
107658	417	13	47	6206	1	0	t
107627	417	13	16	6206	1	0	t
107577	417	12	16	6205	1	0	t
107529	417	11	18	6204	1	0	t
107628	417	13	17	6206	1	0	t
107578	417	12	17	6205	1	0	f
107629	417	13	18	6206	1	0	t
107630	417	13	19	6206	1	0	t
107581	417	12	20	6205	1	0	t
107530	417	11	19	6204	1	0	f
107631	417	13	20	6206	1	0	t
107632	417	13	21	6206	1	0	t
107582	417	12	21	6205	1	0	t
107583	417	12	22	6205	1	0	t
107533	417	11	22	6204	1	0	t
107534	417	11	23	6204	1	0	t
107535	417	11	24	6204	1	0	t
107584	417	12	23	6205	1	0	f
107635	417	13	24	6206	1	0	t
107636	417	13	25	6206	1	0	t
107536	417	11	25	6204	1	0	t
107587	417	12	26	6205	1	0	t
107659	417	13	48	6206	1	0	f
107637	417	13	26	6206	1	0	t
107638	417	13	27	6206	1	0	t
107588	417	12	27	6205	1	0	t
107539	417	11	28	6204	1	0	t
107660	417	13	49	6206	1	0	t
107540	417	11	29	6204	1	0	t
107639	417	13	28	6206	1	0	t
107640	417	13	29	6206	1	0	f
107591	417	12	30	6205	1	0	t
107641	417	13	30	6206	1	0	t
107560	417	11	49	6204	1	2	t
107692	417	14	31	6207	1	0	t
107742	417	15	31	6208	2	1	f
107693	417	14	32	6207	1	0	t
107694	417	14	33	6207	1	0	t
107893	417	18	32	6211	3	0	t
107695	417	14	34	6207	1	0	t
107744	417	15	33	6208	3	0	t
107696	417	14	35	6207	1	0	t
107745	417	15	34	6208	1	2	t
107819	417	17	8	6210	1	0	t
107820	417	17	9	6210	1	0	t
107719	417	15	8	6208	3	0	t
107671	417	14	10	6207	1	0	t
107697	417	14	36	6207	1	0	f
107746	417	15	35	6208	2	0	t
107796	417	16	35	6209	3	0	t
107698	417	14	37	6207	1	0	t
107747	417	15	36	6208	1	3	t
107699	417	14	38	6207	1	0	t
107748	417	15	37	6208	3	0	t
107798	417	16	37	6209	2	3	t
107700	417	14	39	6207	1	0	f
107749	417	15	38	6208	1	2	t
107800	417	16	39	6209	1	2	t
107701	417	14	40	6207	1	0	t
107720	417	15	9	6208	1	2	t
107672	417	14	11	6207	1	0	t
107821	417	17	10	6210	1	0	t
107822	417	17	11	6210	1	0	f
107702	417	14	41	6207	1	0	f
107801	417	16	40	6209	2	3	t
107703	417	14	42	6207	1	0	f
107802	417	16	41	6209	3	0	t
107752	417	15	41	6208	3	1	f
107704	417	14	43	6207	1	0	t
107803	417	16	42	6209	1	2	t
107755	417	15	44	6208	2	0	t
107754	417	15	43	6208	1	2	t
107706	417	14	45	6207	3	0	t
107705	417	14	44	6207	1	3	t
107823	417	17	12	6210	1	0	t
107722	417	15	11	6208	1	3	t
107673	417	14	12	6207	1	0	t
107674	417	14	13	6207	1	0	f
107707	417	14	46	6207	1	0	t
107756	417	15	45	6208	1	2	t
107806	417	16	45	6209	1	2	t
107708	417	14	47	6207	1	0	t
107757	417	15	46	6208	2	0	t
107723	417	15	12	6208	3	0	t
107675	417	14	14	6207	1	0	t
107713	417	15	2	6208	2	1	t
107762	417	16	1	6209	1	2	t
107824	417	17	13	6210	1	0	f
107715	417	15	4	6208	3	0	t
107813	417	17	2	6210	1	3	t
107714	417	15	3	6208	1	3	t
107815	417	17	4	6210	1	2	t
107716	417	15	5	6208	1	0	t
107717	417	15	6	6208	1	0	t
107816	417	17	5	6210	2	0	f
107774	417	16	13	6209	1	2	t
107818	417	17	7	6210	1	0	t
107817	417	17	6	6210	2	0	t
107718	417	15	7	6208	1	3	t
107676	417	14	15	6207	1	0	t
107825	417	17	14	6210	1	2	t
107677	417	14	16	6207	1	0	t
107775	417	16	14	6209	2	3	t
107826	417	17	15	6210	2	0	t
107726	417	15	15	6208	1	3	t
107678	417	14	17	6207	1	2	t
107777	417	16	16	6209	1	2	t
107679	417	14	18	6207	2	0	t
107728	417	15	17	6208	1	2	t
107729	417	15	18	6208	2	0	t
107680	417	14	19	6207	1	0	t
107681	417	14	20	6207	1	0	f
107730	417	15	19	6208	1	3	t
107731	417	15	20	6208	3	0	t
107682	417	14	21	6207	1	0	t
107683	417	14	22	6207	1	0	t
107782	417	16	21	6209	1	2	t
107808	417	16	47	6209	3	0	t
107783	417	16	22	6209	2	3	t
107684	417	14	23	6207	1	0	t
107784	417	16	23	6209	3	0	t
107685	417	14	24	6207	1	0	f
107686	417	14	25	6207	1	0	t
107785	417	16	24	6209	1	2	t
107687	417	14	26	6207	1	0	t
107736	417	15	25	6208	1	3	t
107737	417	15	26	6208	3	0	t
107688	417	14	27	6207	1	0	t
107788	417	16	27	6209	1	2	t
107689	417	14	28	6207	1	0	t
107690	417	14	29	6207	1	0	t
107789	417	16	28	6209	2	3	t
107709	417	14	48	6207	1	2	t
107691	417	14	30	6207	1	0	t
107790	417	16	29	6209	3	0	t
107791	417	16	30	6209	1	2	t
107710	417	14	49	6207	2	0	t
107809	417	16	48	6209	1	2	t
107760	417	15	49	6208	1	2	t
107810	417	16	49	6209	2	3	t
107842	417	17	31	6210	1	0	t
107942	417	19	31	6212	1	3	t
107843	417	17	32	6210	1	0	t
107943	417	19	32	6212	3	0	t
107844	417	17	33	6210	1	0	t
107845	417	17	34	6210	1	0	t
107944	417	19	33	6212	1	0	f
107919	417	19	8	6212	1	2	t
107920	417	19	9	6212	2	0	t
107969	417	20	8	6213	2	1	f
107970	417	20	9	6213	2	1	t
107921	417	19	10	6212	1	0	t
107945	417	19	34	6212	1	0	t
107846	417	17	35	6210	1	0	t
107895	417	18	34	6211	1	3	t
107847	417	17	36	6210	1	0	t
107946	417	19	35	6212	1	3	t
107848	417	17	37	6210	1	0	t
107897	417	18	36	6211	1	0	f
107849	417	17	38	6210	1	0	t
107898	417	18	37	6211	1	3	t
107950	417	19	39	6212	1	0	t
107949	417	19	38	6212	1	0	f
107899	417	18	38	6211	3	0	t
107922	417	19	11	6212	1	0	t
107171	417	4	10	6197	0	2	f
107971	417	20	10	6213	2	1	f
107923	417	19	12	6212	1	0	t
107850	417	17	39	6210	1	0	t
107851	417	17	40	6210	1	0	t
107951	417	19	40	6212	1	0	t
107852	417	17	41	6210	1	0	t
107952	417	19	41	6212	1	0	t
107953	417	19	42	6212	1	0	t
107853	417	17	42	6210	1	0	t
107854	417	17	43	6210	1	0	t
107903	417	18	42	6211	1	0	t
107954	417	19	43	6212	1	0	t
107955	417	19	44	6212	1	0	t
107973	417	20	12	6213	2	1	f
107924	417	19	13	6212	1	0	t
107873	417	18	12	6211	1	3	t
107974	417	20	13	6213	2	1	f
107925	417	19	14	6212	1	0	t
107905	417	18	44	6211	1	0	t
107857	417	17	46	6210	1	0	t
107956	417	19	45	6212	1	0	t
107906	417	18	45	6211	1	0	f
107858	417	17	47	6210	1	0	t
107957	417	19	46	6212	1	0	t
107907	417	18	46	6211	1	3	t
107863	417	18	2	6211	1	0	t
107912	417	19	1	6212	2	3	t
107875	417	18	14	6211	3	0	f
107913	417	19	2	6212	3	0	t
107864	417	18	3	6211	1	3	t
107965	417	20	4	6213	2	0	t
107926	417	19	15	6212	1	0	t
107966	417	20	5	6213	0	1	f
107915	417	19	4	6212	1	2	t
107916	417	19	5	6212	2	0	f
107867	417	18	6	6211	1	0	t
107968	417	20	7	6213	0	1	t
107967	417	20	6	6213	0	1	f
107868	417	18	7	6211	1	3	t
107958	417	19	47	6212	1	0	t
107876	417	18	15	6211	3	1	f
107927	417	19	16	6212	1	0	t
107828	417	17	17	6210	1	0	t
107827	417	17	16	6210	1	0	t
107928	417	19	17	6212	1	0	f
107929	417	19	18	6212	1	0	t
107829	417	17	18	6210	1	0	t
107830	417	17	19	6210	1	0	t
107879	417	18	18	6211	1	3	t
107930	417	19	19	6212	1	0	f
107831	417	17	20	6210	1	0	t
107981	417	20	20	6213	2	1	f
107832	417	17	21	6210	1	0	t
107931	417	19	20	6212	1	3	t
107881	417	18	20	6211	3	1	t
107933	417	19	22	6212	1	0	t
107982	417	20	21	6213	2	1	t
107883	417	18	22	6211	1	0	t
107884	417	18	23	6211	1	0	t
107833	417	17	22	6210	1	0	f
107835	417	17	24	6210	1	0	t
107934	417	19	23	6212	1	0	t
107859	417	17	48	6210	1	0	t
107935	417	19	24	6212	1	0	f
107836	417	17	25	6210	1	0	t
107936	417	19	25	6212	1	3	t
107837	417	17	26	6210	1	0	t
107937	417	19	26	6212	3	0	t
107838	417	17	27	6210	1	0	t
107839	417	17	28	6210	1	0	t
107938	417	19	27	6212	1	3	t
107840	417	17	29	6210	1	0	t
107939	417	19	28	6212	3	0	t
107841	417	17	30	6210	1	0	t
107940	417	19	29	6212	1	0	t
107959	417	19	48	6212	1	0	t
107960	417	19	49	6212	1	0	t
107941	417	19	30	6212	1	0	f
107860	417	17	49	6210	1	0	t
108092	417	22	31	6215	2	0	t
108093	417	22	32	6215	0	1	t
107992	417	20	31	6213	2	1	t
108043	417	21	32	6214	2	0	t
108044	417	21	33	6214	0	1	t
108119	417	23	8	6216	0	1	t
108070	417	22	9	6215	2	1	f
108069	417	22	8	6215	2	1	f
107995	417	20	34	6213	0	1	f
108094	417	22	33	6215	2	3	t
108020	417	21	9	6214	2	3	t
108071	417	22	10	6215	2	1	f
108045	417	21	34	6214	2	1	t
107996	417	20	35	6213	0	1	f
108095	417	22	34	6215	3	1	f
108046	417	21	35	6214	2	1	t
107997	417	20	36	6213	0	1	t
108097	417	22	36	6215	3	1	t
108098	417	22	37	6215	2	1	f
107998	417	20	37	6213	2	1	f
107999	417	20	38	6213	2	1	t
108099	417	22	38	6215	2	1	t
108021	417	21	10	6214	3	1	t
108072	417	22	11	6215	2	1	t
108022	417	21	11	6214	2	1	f
108100	417	22	39	6215	2	0	t
108049	417	21	38	6214	3	2	f
108000	417	20	39	6213	2	1	f
108101	417	22	40	6215	0	1	t
108001	417	20	40	6213	2	1	f
108102	417	22	41	6215	2	1	f
108002	417	20	41	6213	2	3	t
108103	417	22	42	6215	2	1	f
108053	417	21	42	6214	3	1	f
108104	417	22	43	6215	2	1	f
108003	417	20	42	6213	3	1	f
108123	417	23	12	6216	0	1	t
108023	417	21	12	6214	2	0	t
108024	417	21	13	6214	0	2	t
108073	417	22	12	6215	2	3	t
108124	417	23	13	6216	2	0	t
108125	417	23	14	6216	0	1	t
108054	417	21	43	6214	3	1	t
108055	417	21	44	6214	2	1	f
108106	417	22	45	6215	2	1	t
108105	417	22	44	6215	2	1	f
108056	417	21	45	6214	2	1	f
108107	417	22	46	6215	2	0	t
108057	417	21	46	6214	2	1	t
108108	417	22	47	6215	0	1	t
108007	417	20	46	6213	2	1	f
108058	417	21	47	6214	2	1	f
108112	417	23	1	6216	2	1	t
108063	417	22	2	6215	0	1	f
108064	417	22	3	6215	0	1	t
108013	417	21	2	6214	2	1	f
108015	417	21	4	6214	2	0	t
108126	417	23	15	6216	2	0	t
108116	417	23	5	6216	0	1	t
108115	417	23	4	6216	3	0	t
108016	417	21	5	6214	0	1	f
108017	417	21	6	6214	0	2	f
108075	417	22	14	6215	2	1	f
108018	417	21	7	6214	0	1	t
108067	417	22	6	6215	2	1	t
108009	417	20	48	6213	3	1	f
108068	417	22	7	6215	2	1	f
108076	417	22	15	6215	2	1	t
108127	417	23	16	6216	0	1	t
108077	417	22	16	6215	2	0	t
108078	417	22	17	6215	0	1	t
108128	417	23	17	6216	2	1	f
108129	417	23	18	6216	2	0	t
108130	417	23	19	6216	0	1	t
108079	417	22	18	6215	2	1	f
108131	417	23	20	6216	2	0	t
108080	417	22	19	6215	2	1	f
108132	417	23	21	6216	0	1	t
108031	417	21	20	6214	2	0	t
108032	417	21	21	6214	0	1	f
108033	417	21	22	6214	0	1	t
108059	417	21	48	6214	2	3	t
108133	417	23	22	6216	2	0	f
108083	417	22	22	6215	2	1	f
108034	417	21	23	6214	2	1	t
107985	417	20	24	6213	0	1	t
108134	417	23	23	6216	2	1	t
108010	417	20	49	6213	3	1	t
108136	417	23	25	6216	0	1	t
108135	417	23	24	6216	2	0	t
107986	417	20	25	6213	2	0	t
107987	417	20	26	6213	0	1	f
108137	417	23	26	6216	2	1	t
107988	417	20	27	6213	0	1	t
108037	417	21	26	6214	3	1	f
108138	417	23	27	6216	2	1	t
108038	417	21	27	6214	3	1	t
107989	417	20	28	6213	2	1	f
107990	417	20	29	6213	2	1	f
108039	417	21	28	6214	2	1	f
108089	417	22	28	6215	2	1	f
108060	417	21	49	6214	3	1	f
108040	417	21	29	6214	2	3	t
108091	417	22	30	6215	2	1	t
107991	417	20	30	6213	2	1	f
108242	417	25	31	6218	0	1	t
108219	417	25	8	6218	0	1	f
108220	417	25	9	6218	0	1	t
108169	417	24	8	6217	3	1	t
108271	417	26	10	6219	0	1	t
108170	417	24	9	6217	2	0	t
108292	417	26	31	6219	2	3	t
108143	417	23	32	6216	0	1	t
108244	417	25	33	6218	0	1	t
108193	417	24	32	6217	2	0	t
108243	417	25	32	6218	2	0	t
108145	417	23	34	6216	2	0	t
108194	417	24	33	6217	0	1	t
108144	417	23	33	6216	2	1	f
108245	417	25	34	6218	2	0	t
108246	417	25	35	6218	0	1	t
108195	417	24	34	6217	2	1	f
108146	417	23	35	6216	0	1	t
108147	417	23	36	6216	2	0	t
108172	417	24	11	6217	0	2	t
108171	417	24	10	6217	0	1	f
108173	417	24	12	6217	2	0	t
108272	417	26	11	6219	2	1	f
108196	417	24	35	6217	2	3	t
108247	417	25	36	6218	2	0	t
108248	417	25	37	6218	0	1	t
108249	417	25	38	6218	2	0	t
108148	417	23	37	6216	0	1	t
108198	417	24	37	6217	2	3	t
108149	417	23	38	6216	2	1	t
108250	417	25	39	6218	0	1	t
108251	417	25	40	6218	2	0	t
108150	417	23	39	6216	2	1	f
108252	417	25	41	6218	0	1	t
108151	417	23	40	6216	2	0	t
108223	417	25	12	6218	0	3	t
108174	417	24	13	6217	0	1	t
108273	417	26	12	6219	2	1	f
108224	417	25	13	6218	3	1	f
108253	417	25	42	6218	2	0	t
108152	417	23	41	6216	0	1	t
108202	417	24	41	6217	2	3	t
108153	417	23	42	6216	2	1	t
108254	417	25	43	6218	0	1	t
108255	417	25	44	6218	2	0	t
108154	417	23	43	6216	2	0	f
108155	417	23	44	6216	2	1	t
108256	417	25	45	6218	0	1	t
108175	417	24	14	6217	2	1	f
108156	417	23	45	6216	2	1	f
108162	417	24	1	6217	2	0	t
108163	417	24	2	6217	0	1	t
108225	417	25	14	6218	3	1	f
108213	417	25	2	6218	0	3	t
108164	417	24	3	6217	2	0	f
108265	417	26	4	6219	0	1	f
108226	417	25	15	6218	3	0	t
108215	417	25	4	6218	3	1	f
108266	417	26	5	6219	0	3	f
108216	417	25	5	6218	3	1	f
108267	417	26	6	6219	0	1	t
108218	417	25	7	6218	0	1	f
108217	417	25	6	6218	3	0	t
108157	417	23	46	6216	2	0	t
108268	417	26	7	6219	2	1	f
108206	417	24	45	6217	3	1	f
108176	417	24	15	6217	2	3	t
108227	417	25	16	6218	0	1	t
108278	417	26	17	6219	0	2	f
108277	417	26	16	6219	3	0	t
108228	417	25	17	6218	2	3	t
108279	417	26	18	6219	0	1	t
108179	417	24	18	6217	2	0	t
108181	417	24	20	6217	3	1	f
108180	417	24	19	6217	0	3	t
108280	417	26	19	6219	2	1	f
108231	417	25	20	6218	2	3	t
108232	417	25	21	6218	3	0	t
108233	417	25	22	6218	0	1	t
108182	417	24	21	6217	3	1	t
108257	417	25	46	6218	2	0	t
108184	417	24	23	6217	2	1	f
108183	417	24	22	6217	2	1	f
108234	417	25	23	6218	2	1	f
108235	417	25	24	6218	2	0	t
108236	417	25	25	6218	0	1	t
108285	417	26	24	6219	3	0	t
108258	417	25	47	6218	0	1	t
108286	417	26	25	6219	0	1	f
108287	417	26	26	6219	0	1	t
108238	417	25	27	6218	0	1	t
108237	417	25	26	6218	2	0	t
108288	417	26	27	6219	2	1	f
108139	417	23	28	6216	2	0	t
108239	417	25	28	6218	2	0	t
108240	417	25	29	6218	0	1	t
108241	417	25	30	6218	2	0	t
108140	417	23	29	6216	0	1	t
108158	417	23	47	6216	0	1	t
108259	417	25	48	6218	2	0	t
108291	417	26	30	6219	2	1	f
108141	417	23	30	6216	2	1	f
108260	417	25	49	6218	0	1	t
108159	417	23	48	6216	2	1	f
108210	417	24	49	6217	0	1	t
108160	417	23	49	6216	2	1	t
108419	417	29	8	6222	2	1	f
108369	417	28	8	6221	3	1	f
108370	417	28	9	6221	3	0	t
108420	417	29	9	6222	2	1	t
108371	417	28	10	6221	0	1	t
108120	417	23	9	6216	2	3	t
108442	417	29	31	6222	0	1	t
107343	417	7	32	6200	0	3	t
108342	417	27	31	6220	2	1	f
107293	417	6	32	6199	0	3	t
107894	417	18	33	6211	1	0	f
107344	417	7	33	6200	0	3	t
108395	417	28	34	6221	0	1	t
108295	417	26	34	6219	2	0	t
108296	417	26	35	6219	0	1	f
108445	417	29	34	6222	2	1	f
108372	417	28	11	6221	2	0	t
108421	417	29	10	6222	2	1	f
108422	417	29	11	6222	2	1	t
108323	417	27	12	6220	0	1	t
108347	417	27	36	6220	0	1	t
108396	417	28	35	6221	2	1	f
108397	417	28	36	6221	2	0	t
108398	417	28	37	6221	0	1	f
108297	417	26	36	6219	0	3	t
108399	417	28	38	6221	0	1	t
108348	417	27	37	6220	2	0	t
108298	417	26	37	6219	3	1	t
108350	417	27	39	6220	2	0	t
108349	417	27	38	6220	0	1	t
108449	417	29	38	6222	3	1	f
108374	417	28	13	6221	2	0	f
108373	417	28	12	6221	0	1	t
108425	417	29	14	6222	2	1	t
108324	417	27	13	6220	2	1	f
108400	417	28	39	6221	2	1	t
108351	417	27	40	6220	0	1	t
108450	417	29	39	6222	3	1	f
108401	417	28	40	6221	2	1	f
108402	417	28	41	6221	2	0	t
108301	417	26	40	6219	3	1	f
108403	417	28	42	6221	0	1	t
108302	417	26	41	6219	3	0	t
108352	417	27	41	6220	2	1	f
108303	417	26	42	6219	0	1	t
108354	417	27	43	6220	2	0	t
108355	417	27	44	6220	0	1	t
108412	417	29	1	6222	2	1	f
108375	417	28	14	6221	2	1	t
108313	417	27	2	6220	0	1	f
108304	417	26	43	6219	2	0	f
108413	417	29	2	6222	2	0	t
108314	417	27	3	6220	0	3	t
108415	417	29	4	6222	0	1	f
108365	417	28	4	6221	2	0	t
108366	417	28	5	6221	0	1	t
108317	417	27	6	6220	0	1	f
108416	417	29	5	6222	0	3	t
108318	417	27	7	6220	0	3	t
108367	417	28	6	6221	2	1	f
108426	417	29	15	6222	2	1	f
108368	417	28	7	6221	2	3	t
108376	417	28	15	6221	2	3	t
108327	417	27	16	6220	0	1	f
108328	417	27	17	6220	0	1	t
108427	417	29	16	6222	2	1	t
108428	417	29	17	6222	2	1	t
108404	417	28	43	6221	2	3	t
108379	417	28	18	6221	2	0	t
108380	417	28	19	6221	0	1	t
108429	417	29	18	6222	2	1	f
108430	417	29	19	6222	2	1	f
108331	417	27	20	6220	2	0	t
108332	417	27	21	6220	0	1	t
108381	417	28	20	6221	2	1	t
108356	417	27	45	6220	2	0	t
108382	417	28	21	6221	2	3	t
108333	417	27	22	6220	2	0	t
108334	417	27	23	6220	0	1	t
108433	417	29	22	6222	2	1	f
108335	417	27	24	6220	2	0	t
108434	417	29	23	6222	2	1	t
108305	417	26	44	6219	2	1	t
108336	417	27	25	6220	0	1	t
108435	417	29	24	6222	2	1	f
108387	417	28	26	6221	0	1	t
108436	417	29	25	6222	2	1	f
108338	417	27	27	6220	0	1	t
108337	417	27	26	6220	2	0	t
108339	417	27	28	6220	2	0	t
108388	417	28	27	6221	2	1	f
108389	417	28	28	6221	2	0	t
108390	417	28	29	6221	0	1	t
108441	417	29	30	6222	2	0	t
108340	417	27	29	6220	0	1	t
108341	417	27	30	6220	2	0	f
108406	417	28	45	6221	3	1	f
108357	417	27	46	6220	0	1	t
108407	417	28	46	6221	3	0	t
108408	417	28	47	6221	0	1	t
108358	417	27	47	6220	2	0	t
108359	417	27	48	6220	0	1	t
108409	417	28	48	6221	2	1	t
108360	417	27	49	6220	2	0	t
108310	417	26	49	6219	2	1	t
108410	417	28	49	6221	2	1	f
108469	417	30	8	6223	2	1	t
108470	417	30	9	6223	2	1	t
108519	417	31	8	6224	2	1	f
108520	417	31	9	6224	2	1	f
108471	417	30	10	6223	2	1	t
108492	417	30	31	6223	2	0	t
108493	417	30	32	6223	0	1	t
108542	417	31	31	6224	2	1	f
108593	417	32	32	6225	0	1	t
108494	417	30	33	6223	2	1	f
108594	417	32	33	6225	2	1	f
108495	417	30	34	6223	2	0	f
108545	417	31	34	6224	2	1	f
108496	417	30	35	6223	2	1	t
108595	417	32	34	6225	2	3	t
108546	417	31	35	6224	2	1	f
108521	417	31	10	6224	2	1	f
108522	417	31	11	6224	2	1	f
108472	417	30	11	6223	2	1	f
108523	417	31	12	6224	2	1	t
108547	417	31	36	6224	2	1	t
108497	417	30	36	6223	2	1	t
108498	417	30	37	6223	2	1	f
108548	417	31	37	6224	2	1	f
108549	417	31	38	6224	2	1	t
108599	417	32	38	6225	2	1	f
108600	417	32	39	6225	2	0	f
108499	417	30	38	6223	2	3	t
108550	417	31	39	6224	2	1	f
108502	417	30	41	6223	2	1	t
108551	417	31	40	6224	2	1	t
108524	417	31	13	6224	2	1	t
108573	417	32	12	6225	3	1	t
108473	417	30	12	6223	2	3	t
108525	417	31	14	6224	2	1	f
108574	417	32	13	6225	2	3	t
108501	417	30	40	6223	2	1	f
108503	417	30	42	6223	2	1	f
108552	417	31	41	6224	2	1	f
108452	417	29	41	6222	3	1	f
108504	417	30	43	6223	2	0	f
108553	417	31	42	6224	2	1	f
108603	417	32	42	6225	3	2	f
108455	417	29	44	6222	2	1	f
108454	417	29	43	6222	2	1	t
108554	417	31	43	6224	2	1	f
108505	417	30	44	6223	2	1	f
108462	417	30	1	6223	2	0	f
108513	417	31	2	6224	2	1	t
108575	417	32	14	6225	3	1	f
108514	417	31	3	6224	2	1	t
108463	417	30	2	6223	2	3	t
108576	417	32	15	6225	3	0	t
108515	417	31	4	6224	2	1	t
108465	417	30	4	6223	3	1	f
108466	417	30	5	6223	3	0	t
108516	417	31	5	6224	2	1	t
108467	417	30	6	6223	0	1	f
108517	417	31	6	6224	2	1	f
108468	417	30	7	6223	0	1	t
108577	417	32	16	6225	0	1	t
108518	417	31	7	6224	2	1	f
108555	417	31	44	6224	2	1	f
108526	417	31	15	6224	2	1	t
108578	417	32	17	6225	2	0	t
108477	417	30	16	6223	0	1	t
108579	417	32	18	6225	0	1	t
108556	417	31	45	6224	2	0	t
108478	417	30	17	6223	2	1	f
108529	417	31	18	6224	2	1	f
108530	417	31	19	6224	2	1	f
108580	417	32	19	6225	2	1	f
108581	417	32	20	6225	2	0	t
108481	417	30	20	6223	2	1	t
108582	417	32	21	6225	0	1	t
108482	417	30	21	6223	2	1	t
108583	417	32	22	6225	2	0	f
108585	417	32	24	6225	2	1	t
108483	417	30	22	6223	2	1	f
108584	417	32	23	6225	2	1	f
108456	417	29	45	6222	2	1	t
108484	417	30	23	6223	2	3	t
108535	417	31	24	6224	2	1	f
108487	417	30	26	6223	2	0	t
108536	417	31	25	6224	2	1	f
108557	417	31	46	6224	0	2	t
108586	417	32	25	6225	2	1	f
108537	417	31	26	6224	2	1	t
108488	417	30	27	6223	0	1	f
108506	417	30	45	6223	2	3	t
108489	417	30	28	6223	0	1	t
108538	417	31	27	6224	2	1	f
108491	417	30	30	6223	2	1	f
108539	417	31	28	6224	2	1	t
108490	417	30	29	6223	2	1	t
108540	417	31	29	6224	2	1	f
108541	417	31	30	6224	2	1	f
108457	417	29	46	6222	2	1	f
108458	417	29	47	6222	2	1	t
108507	417	30	46	6223	3	1	f
108558	417	31	47	6224	2	1	f
108459	417	29	48	6222	2	1	f
108560	417	31	49	6224	2	1	f
108559	417	31	48	6224	2	1	f
108460	417	29	49	6222	2	1	f
108619	417	33	8	6226	2	1	f
108669	417	34	8	6227	2	1	f
108670	417	34	9	6227	2	1	t
108642	417	33	31	6226	3	0	t
108643	417	33	32	6226	0	1	t
109070	417	42	9	6235	3	2	t
108742	417	35	31	6228	2	1	f
108644	417	33	33	6226	2	0	t
107393	417	8	32	6201	0	3	t
107243	417	5	32	6198	0	3	f
108645	417	33	34	6226	0	1	f
107294	417	6	33	6199	0	3	t
107394	417	8	33	6201	0	3	f
108646	417	33	35	6226	0	1	t
108697	417	34	36	6227	0	1	t
108696	417	34	35	6227	0	1	f
108647	417	33	36	6226	2	1	f
108648	417	33	37	6226	2	0	t
108721	417	35	10	6228	2	1	t
108671	417	34	10	6227	2	1	f
108672	417	34	11	6227	2	0	t
108673	417	34	12	6227	0	1	t
108698	417	34	37	6227	2	1	f
108649	417	33	38	6226	0	1	t
108748	417	35	37	6228	2	1	f
108700	417	34	39	6227	0	1	t
108699	417	34	38	6227	2	0	t
108650	417	33	39	6226	2	0	t
108651	417	33	40	6226	0	1	t
108701	417	34	40	6227	2	0	f
108752	417	35	41	6228	0	1	t
108652	417	33	41	6226	2	0	t
108722	417	35	11	6228	2	1	t
108723	417	35	12	6228	2	1	f
108674	417	34	13	6227	2	0	t
108623	417	33	12	6226	3	2	f
108653	417	33	42	6226	0	1	t
108702	417	34	41	6227	2	1	t
108704	417	34	43	6227	2	0	f
108753	417	35	42	6228	2	1	f
108654	417	33	43	6226	2	0	f
108655	417	33	44	6226	2	1	f
108756	417	35	45	6228	0	2	f
108705	417	34	44	6227	2	1	f
108757	417	35	46	6228	0	1	t
108706	417	34	45	6227	2	1	t
108675	417	34	14	6227	0	1	t
108724	417	35	13	6228	2	1	t
108663	417	34	2	6227	0	1	t
108762	417	36	1	6229	2	0	f
108714	417	35	3	6228	0	1	t
108713	417	35	2	6228	0	1	f
108665	417	34	4	6227	2	0	t
108664	417	34	3	6227	2	1	t
108615	417	33	4	6226	2	1	t
108666	417	34	5	6227	0	1	f
108617	417	33	6	6226	0	1	t
108616	417	33	5	6226	2	0	t
108625	417	33	14	6226	0	1	t
108668	417	34	7	6227	2	1	t
108667	417	34	6	6227	0	1	t
108618	417	33	7	6226	2	1	t
108607	417	32	46	6225	0	1	t
108626	417	33	15	6226	2	0	t
108725	417	35	14	6228	2	1	t
108627	417	33	16	6226	0	1	t
108676	417	34	15	6227	2	1	f
108677	417	34	16	6227	2	0	f
108678	417	34	17	6227	2	0	t
108628	417	33	17	6226	2	0	t
108679	417	34	18	6227	0	1	t
108658	417	33	47	6226	0	1	t
108629	417	33	18	6226	0	1	t
108680	417	34	19	6227	2	0	f
108707	417	34	46	6227	2	1	f
108630	417	33	19	6226	2	0	f
108681	417	34	20	6227	2	0	f
108733	417	35	22	6228	0	1	t
108631	417	33	20	6226	2	1	t
108682	417	34	21	6227	2	1	t
108633	417	33	22	6226	2	0	f
108684	417	34	23	6227	2	1	f
108610	417	32	49	6225	2	1	t
108608	417	32	47	6225	2	1	t
108634	417	33	23	6226	2	1	f
108635	417	33	24	6226	2	0	t
108736	417	35	25	6228	0	1	t
108685	417	34	24	6227	2	0	f
108637	417	33	26	6226	0	1	t
108636	417	33	25	6226	0	1	f
108738	417	35	27	6228	0	1	f
108737	417	35	26	6228	2	0	t
108739	417	35	28	6228	0	1	t
108688	417	34	27	6227	2	1	f
108689	417	34	28	6227	2	1	f
108740	417	35	29	6228	2	1	f
108758	417	35	47	6228	2	1	f
108640	417	33	29	6226	3	1	f
108741	417	35	30	6228	2	1	f
108641	417	33	30	6226	3	1	f
108609	417	32	48	6225	2	1	f
108709	417	34	48	6227	2	1	f
108659	417	33	48	6226	2	1	f
108710	417	34	49	6227	2	1	f
108760	417	35	49	6228	2	1	f
108769	417	36	8	6229	0	3	t
108819	417	37	8	6230	2	3	t
108869	417	38	8	6231	3	2	f
108870	417	38	9	6231	3	0	t
108842	417	37	31	6230	2	1	t
108792	417	36	31	6229	2	1	f
109894	417	58	33	6251	0	2	t
108843	417	37	32	6230	2	1	t
108443	417	29	32	6222	2	1	t
108894	417	38	33	6231	0	3	t
107244	417	5	33	6198	0	3	t
108895	417	38	34	6231	3	1	f
108796	417	36	35	6229	0	1	t
108846	417	37	35	6230	2	1	f
108871	417	38	10	6231	0	3	t
108770	417	36	9	6229	3	1	f
108820	417	37	9	6230	3	1	f
108872	417	38	11	6231	3	1	f
108771	417	36	10	6229	3	1	f
108898	417	38	37	6231	2	1	f
108896	417	38	35	6231	3	1	t
108797	417	36	36	6229	2	1	f
108847	417	37	36	6230	2	3	t
108899	417	38	38	6231	2	0	t
108848	417	37	37	6230	3	1	f
108798	417	36	37	6229	2	3	t
108849	417	37	38	6230	3	1	f
108900	417	38	39	6231	0	2	t
108851	417	37	40	6230	0	1	t
108850	417	37	39	6230	3	0	t
108823	417	37	12	6230	2	1	f
108822	417	37	11	6230	3	2	t
108901	417	38	40	6231	2	3	t
108824	417	37	13	6230	2	0	t
108773	417	36	12	6229	3	1	t
108802	417	36	41	6229	2	1	t
108852	417	37	41	6230	2	1	f
108853	417	37	42	6230	2	0	t
108902	417	38	41	6231	3	1	f
108803	417	36	42	6229	2	1	t
108854	417	37	43	6230	0	1	t
108904	417	38	43	6231	3	0	t
108905	417	38	44	6231	0	1	t
108806	417	36	45	6229	0	1	t
108855	417	37	44	6230	2	1	f
108857	417	37	46	6230	0	1	t
108856	417	37	45	6230	2	0	t
108873	417	38	12	6231	3	2	f
108825	417	37	14	6230	0	1	t
108774	417	36	13	6229	2	1	t
108875	417	38	14	6231	0	2	f
108876	417	38	15	6231	0	1	t
108913	417	39	2	6232	0	1	f
108812	417	37	1	6230	2	1	t
108827	417	37	16	6230	0	1	f
108826	417	37	15	6230	2	0	t
108914	417	39	3	6232	0	1	f
108864	417	38	3	6231	2	0	t
108915	417	39	4	6232	0	2	t
108865	417	38	4	6231	0	3	t
108766	417	36	5	6229	2	0	t
108765	417	36	4	6229	2	1	t
108916	417	39	5	6232	2	1	f
108767	417	36	6	6229	0	1	f
108828	417	37	17	6230	0	1	t
108917	417	39	6	6232	2	1	f
108768	417	36	7	6229	0	1	f
108867	417	38	6	6231	3	2	t
108918	417	39	7	6232	2	0	t
108877	417	38	16	6231	2	1	t
108777	417	36	16	6229	3	1	f
108878	417	38	17	6231	2	1	t
108779	417	36	18	6229	3	0	t
108906	417	38	45	6231	2	3	t
108879	417	38	18	6231	2	1	f
108780	417	36	19	6229	0	1	t
108880	417	38	19	6231	2	0	f
108881	417	38	20	6231	2	1	f
108782	417	36	21	6229	2	1	f
108781	417	36	20	6229	2	1	f
108882	417	38	21	6231	2	3	t
108783	417	36	22	6229	2	0	t
108784	417	36	23	6229	0	1	t
108833	417	37	22	6230	3	1	t
108785	417	36	24	6229	2	1	t
108807	417	36	46	6229	2	1	f
108858	417	37	47	6230	2	1	t
108835	417	37	24	6230	3	1	f
108886	417	38	25	6231	3	0	f
108786	417	36	25	6229	2	1	f
108787	417	36	26	6229	2	3	t
108887	417	38	26	6231	3	2	f
108838	417	37	27	6230	2	1	f
108839	417	37	28	6230	2	1	t
108788	417	36	27	6229	3	1	t
108790	417	36	29	6229	2	0	t
108789	417	36	28	6229	2	1	f
108859	417	37	48	6230	2	1	t
108840	417	37	29	6230	2	1	t
108791	417	36	30	6229	0	1	t
108841	417	37	30	6230	2	1	t
108808	417	36	47	6229	2	1	f
108910	417	38	49	6231	2	0	t
108809	417	36	48	6229	2	3	t
108860	417	37	49	6230	2	1	f
108810	417	36	49	6229	3	1	f
108969	417	40	8	6233	0	1	t
108942	417	39	31	6232	0	1	t
108943	417	39	32	6232	2	1	t
109042	417	41	31	6234	0	2	t
107993	417	20	32	6213	2	1	t
107994	417	20	33	6213	2	0	t
108995	417	40	34	6233	0	1	t
108444	417	29	33	6222	2	1	t
108996	417	40	35	6233	1	2	t
109045	417	41	34	6234	0	2	t
108945	417	39	34	6232	2	1	t
109020	417	41	9	6234	0	2	t
108919	417	39	8	6232	0	3	t
109021	417	41	10	6234	3	0	t
108970	417	40	9	6233	1	2	t
109046	417	41	35	6234	3	2	f
108997	417	40	36	6233	3	0	t
108998	417	40	37	6233	0	1	t
108947	417	39	36	6232	2	1	f
108948	417	39	37	6232	2	3	t
109049	417	41	38	6234	0	2	t
108999	417	40	38	6233	1	2	t
109000	417	40	39	6233	3	0	t
108949	417	39	38	6232	3	2	t
109001	417	40	40	6233	0	1	t
109050	417	41	39	6234	3	2	f
108920	417	39	9	6232	3	1	f
108971	417	40	10	6233	3	1	f
108921	417	39	10	6232	3	2	f
109022	417	41	11	6234	0	2	t
109052	417	41	41	6234	0	2	t
109051	417	41	40	6234	3	0	t
109002	417	40	41	6233	1	2	t
109003	417	40	42	6233	3	0	t
109004	417	40	43	6233	0	1	t
108953	417	39	42	6232	2	1	t
109053	417	41	42	6234	3	1	f
108954	417	39	43	6232	2	0	f
109055	417	41	44	6234	3	0	t
109005	417	40	44	6233	1	2	t
109056	417	41	45	6234	0	2	t
108973	417	40	12	6233	0	2	t
108972	417	40	11	6233	3	0	t
108922	417	39	11	6232	3	1	t
108924	417	39	13	6232	2	0	f
108923	417	39	12	6232	2	1	t
109007	417	40	46	6233	0	1	t
109006	417	40	45	6233	3	0	t
109023	417	41	12	6234	3	2	f
109012	417	41	1	6234	1	0	t
109063	417	42	2	6235	0	2	t
109064	417	42	3	6235	3	0	t
109013	417	41	2	6234	0	2	t
109065	417	42	4	6235	0	2	f
109066	417	42	5	6235	0	2	t
109015	417	41	4	6234	3	1	f
108967	417	40	6	6233	3	0	t
108974	417	40	13	6233	3	1	f
109016	417	41	5	6234	3	2	f
108957	417	39	46	6232	0	1	f
109017	417	41	6	6234	3	0	t
109018	417	41	7	6234	0	2	t
108968	417	40	7	6233	0	2	f
109025	417	41	14	6234	0	2	f
109074	417	42	13	6235	3	2	t
108975	417	40	14	6233	3	0	t
108958	417	39	47	6232	0	2	f
109057	417	41	46	6234	3	1	f
109026	417	41	15	6234	0	1	t
108976	417	40	15	6233	0	2	t
109027	417	41	16	6234	1	2	t
108977	417	40	16	6233	3	1	f
108978	417	40	17	6233	3	0	t
108979	417	40	18	6233	0	2	t
109028	417	41	17	6234	3	0	f
109029	417	41	18	6234	3	1	f
108980	417	40	19	6233	3	1	t
108930	417	39	19	6232	3	2	f
108931	417	39	20	6232	3	0	t
108981	417	40	20	6233	1	2	t
108932	417	39	21	6232	0	1	t
109032	417	41	21	6234	0	2	t
109033	417	41	22	6234	3	0	t
109008	417	40	47	6233	1	2	t
108984	417	40	23	6233	0	2	t
108933	417	39	22	6232	2	1	f
109034	417	41	23	6234	0	2	f
109035	417	41	24	6234	0	2	t
108986	417	40	25	6233	0	2	f
108985	417	40	24	6233	3	0	t
109059	417	41	48	6234	0	1	t
108987	417	40	26	6233	0	1	t
108936	417	39	25	6232	3	0	t
108937	417	39	26	6232	0	2	t
108988	417	40	27	6233	1	2	t
108989	417	40	28	6233	3	0	t
108938	417	39	27	6232	2	1	f
108939	417	39	28	6232	2	3	t
108990	417	40	29	6233	0	2	f
108991	417	40	30	6233	0	1	t
108940	417	39	29	6232	3	2	f
109009	417	40	48	6233	3	0	t
108941	417	39	30	6232	3	0	t
109010	417	40	49	6233	0	1	t
109060	417	41	49	6234	1	2	t
109192	417	44	31	6237	0	2	t
109142	417	43	31	6236	3	2	t
109094	417	42	33	6235	0	2	t
109193	417	44	32	6237	3	0	t
108743	417	35	32	6228	2	1	f
108543	417	31	32	6224	2	1	f
109194	417	44	33	6237	0	2	f
109195	417	44	34	6237	0	2	t
109169	417	44	8	6237	0	2	f
109170	417	44	9	6237	0	2	f
109219	417	45	8	6238	0	2	f
109221	417	45	10	6238	0	1	t
109220	417	45	9	6238	0	2	f
108620	417	33	9	6226	2	3	t
109095	417	42	34	6235	3	2	f
109096	417	42	35	6235	3	0	t
109097	417	42	36	6235	0	2	t
109196	417	44	35	6237	3	0	f
109198	417	44	37	6237	0	2	t
109197	417	44	36	6237	3	0	t
109148	417	43	37	6236	3	2	t
109199	417	44	38	6237	3	0	t
109098	417	42	37	6235	3	2	t
109200	417	44	39	6237	0	2	t
109149	417	43	38	6236	3	2	f
109102	417	42	41	6235	0	2	t
109172	417	44	11	6237	3	0	t
109171	417	44	10	6237	0	2	t
109222	417	45	11	6238	1	2	t
109173	417	44	12	6237	0	2	t
109150	417	43	39	6236	3	2	f
109201	417	44	40	6237	3	0	f
109151	417	43	40	6236	3	2	t
109203	417	44	42	6237	0	2	t
109202	417	44	41	6237	3	0	t
109152	417	43	41	6236	3	2	f
109204	417	44	43	6237	3	0	t
109103	417	42	42	6235	3	2	f
109205	417	44	44	6237	0	2	t
109154	417	43	43	6236	3	2	f
109206	417	44	45	6237	3	0	t
109175	417	44	14	6237	0	2	f
109123	417	43	12	6236	3	2	f
109174	417	44	13	6237	3	0	t
109155	417	43	44	6236	3	2	f
109124	417	43	13	6236	3	2	f
109207	417	44	46	6237	0	2	t
109106	417	42	45	6235	3	2	t
109156	417	43	45	6236	3	2	f
109107	417	42	46	6235	3	2	f
109208	417	44	47	6237	3	0	t
109176	417	44	15	6237	0	2	t
109225	417	45	14	6238	0	2	f
109162	417	44	1	6237	0	2	t
109213	417	45	2	6238	3	0	t
109163	417	44	2	6237	3	0	f
109214	417	45	3	6238	0	3	t
109165	417	44	4	6237	0	2	t
109166	417	44	5	6237	3	0	t
109115	417	43	4	6236	3	2	f
109167	417	44	6	6237	0	2	t
109116	417	43	5	6236	3	2	f
109217	417	45	6	6238	1	2	t
109218	417	45	7	6238	3	0	t
109168	417	44	7	6237	3	0	t
109127	417	43	16	6236	3	1	t
109126	417	43	15	6236	0	2	t
109226	417	45	15	6238	0	3	t
109209	417	44	48	6237	0	2	t
109177	417	44	16	6237	3	2	f
109178	417	44	17	6237	3	0	t
109227	417	45	16	6238	3	2	f
109128	417	43	17	6236	1	2	t
109179	417	44	18	6237	0	2	t
109130	417	43	19	6236	3	0	t
109129	417	43	18	6236	3	2	f
109229	417	45	18	6238	3	2	f
109180	417	44	19	6237	3	0	t
109181	417	44	20	6237	0	2	t
109080	417	42	19	6235	3	2	t
109158	417	43	47	6236	3	2	f
109131	417	43	20	6236	0	2	t
109182	417	44	21	6237	3	0	t
109183	417	44	22	6237	0	2	t
109132	417	43	21	6236	3	1	f
109133	417	43	22	6236	3	0	t
109134	417	43	23	6236	0	2	f
109184	417	44	23	6237	3	2	t
109135	417	43	24	6236	0	2	t
109185	417	44	24	6237	3	2	f
109086	417	42	25	6235	0	2	t
109136	417	43	25	6236	3	2	t
109188	417	44	27	6237	0	2	f
109137	417	43	26	6236	3	2	f
109087	417	42	26	6235	3	2	f
109210	417	44	49	6237	3	0	t
109088	417	42	27	6235	3	0	t
109189	417	44	28	6237	0	2	t
109089	417	42	28	6235	0	2	t
109190	417	44	29	6237	3	1	f
109191	417	44	30	6237	3	0	t
109090	417	42	29	6235	3	2	t
109159	417	43	48	6236	3	2	f
109091	417	42	30	6235	3	2	t
109110	417	42	49	6235	3	2	f
109160	417	43	49	6236	3	2	f
109242	417	45	31	6238	1	2	t
109293	417	46	32	6239	0	2	t
109342	417	47	31	6240	3	1	t
109294	417	46	33	6239	3	0	t
109343	417	47	32	6240	1	2	t
109295	417	46	34	6239	0	2	t
109344	417	47	33	6240	3	1	f
109319	417	47	8	6240	0	1	t
109270	417	46	9	6239	0	2	f
109269	417	46	8	6239	0	2	f
109320	417	47	9	6240	1	2	t
109271	417	46	10	6239	0	1	t
109245	417	45	34	6238	3	1	f
109246	417	45	35	6238	3	0	t
109345	417	47	34	6240	3	2	t
109247	417	45	36	6238	0	2	t
109296	417	46	35	6239	3	0	f
109347	417	47	36	6240	3	1	f
109248	417	45	37	6238	3	0	t
109348	417	47	37	6240	3	2	f
109249	417	45	38	6238	0	2	t
109299	417	46	38	6239	0	2	f
109300	417	46	39	6239	0	2	t
109322	417	47	11	6240	0	2	f
109321	417	47	10	6240	3	0	t
109323	417	47	12	6240	0	2	f
109349	417	47	38	6240	3	1	f
109250	417	45	39	6238	3	2	t
109351	417	47	40	6240	0	2	t
109301	417	46	40	6239	3	0	t
109302	417	46	41	6239	0	2	f
109303	417	46	42	6239	0	2	t
109352	417	47	41	6240	3	2	t
109304	417	46	43	6239	3	0	t
109353	417	47	42	6240	3	1	f
109253	417	45	42	6238	3	2	f
109354	417	47	43	6240	3	0	t
109255	417	45	44	6238	0	2	t
109272	417	46	11	6239	1	2	t
109273	417	46	12	6239	3	0	t
109324	417	47	13	6240	0	1	t
109373	417	48	12	6241	3	2	f
109307	417	46	46	6239	0	2	t
109355	417	47	44	6240	0	2	t
109256	417	45	45	6238	3	1	f
109356	417	47	45	6240	3	2	f
109258	417	45	47	6238	0	2	t
109257	417	45	46	6238	3	0	t
109357	417	47	46	6240	3	1	t
109309	417	46	48	6239	0	2	f
109274	417	46	13	6239	0	2	t
109275	417	46	14	6239	3	0	t
109262	417	46	1	6239	0	2	t
109263	417	46	2	6239	3	0	t
109264	417	46	3	6239	0	2	t
109313	417	47	2	6240	3	0	t
109365	417	48	4	6241	0	1	f
109308	417	46	47	6239	3	0	t
109265	417	46	4	6239	3	0	t
109266	417	46	5	6239	0	2	t
109317	417	47	6	6240	0	2	f
109366	417	48	5	6241	0	3	t
109268	417	46	7	6239	0	2	f
109267	417	46	6	6239	3	0	t
109325	417	47	14	6240	1	2	t
109318	417	47	7	6240	0	2	f
109276	417	46	15	6239	0	2	t
109377	417	48	16	6241	0	2	t
109326	417	47	15	6240	3	2	t
109328	417	47	17	6240	0	2	t
109327	417	47	16	6240	3	0	t
109378	417	48	17	6241	3	2	t
109279	417	46	18	6239	0	2	t
109379	417	48	18	6241	3	1	t
109380	417	48	19	6241	1	0	t
109231	417	45	20	6238	0	1	t
109280	417	46	19	6239	3	0	t
109381	417	48	20	6241	0	1	t
109333	417	47	22	6240	0	1	t
109281	417	46	20	6239	0	2	t
109382	417	48	21	6241	1	2	t
109260	417	45	49	6238	0	2	t
109232	417	45	21	6238	1	2	t
109259	417	45	48	6238	3	0	t
109283	417	46	22	6239	0	2	t
109284	417	46	23	6239	3	0	t
109334	417	47	23	6240	1	2	t
109285	417	46	24	6239	0	2	t
109235	417	45	24	6238	0	2	t
109336	417	47	25	6240	0	2	f
109335	417	47	24	6240	3	0	t
109286	417	46	25	6239	3	0	t
109236	417	45	25	6238	3	2	t
109337	417	47	26	6240	0	2	t
109287	417	46	26	6239	0	2	f
109288	417	46	27	6239	0	1	t
109237	417	45	26	6238	3	0	t
109239	417	45	28	6238	0	3	f
109338	417	47	27	6240	3	2	f
109289	417	46	28	6239	1	2	t
109240	417	45	29	6238	0	2	f
109310	417	46	49	6239	0	2	f
109290	417	46	29	6239	3	2	f
109241	417	45	30	6238	0	1	t
109341	417	47	30	6240	1	2	t
109392	417	48	31	6241	0	1	t
109493	417	50	32	6243	0	2	t
109442	417	49	31	6242	3	0	t
109519	417	51	8	6244	0	1	t
109420	417	49	9	6242	3	0	t
109419	417	49	8	6242	3	2	f
109520	417	51	9	6244	1	3	t
109443	417	49	32	6242	0	2	t
108544	417	31	33	6224	2	1	f
109393	417	48	32	6241	1	2	t
109394	417	48	33	6241	3	2	f
109395	417	48	34	6241	3	0	t
109444	417	49	33	6242	3	2	f
109445	417	49	34	6242	3	2	f
109396	417	48	35	6241	0	2	f
109397	417	48	36	6241	0	2	t
109496	417	50	35	6243	1	2	t
109421	417	49	10	6242	0	2	t
109472	417	50	11	6243	0	2	f
109371	417	48	10	6241	3	2	f
109422	417	49	11	6242	3	1	t
109446	417	49	35	6242	3	1	t
109448	417	49	37	6242	3	0	t
109497	417	50	36	6243	3	2	t
109499	417	50	38	6243	0	2	t
109498	417	50	37	6243	3	0	t
109398	417	48	37	6241	3	2	f
109449	417	49	38	6242	0	2	f
109450	417	49	39	6242	0	1	t
109401	417	48	40	6241	3	0	t
109400	417	48	39	6241	3	1	f
109402	417	48	41	6241	0	1	t
109451	417	49	40	6242	1	2	t
109473	417	50	12	6243	0	3	t
109423	417	49	12	6242	1	2	t
109523	417	51	12	6244	3	2	f
109474	417	50	13	6243	3	2	f
109452	417	49	41	6242	3	1	f
109403	417	48	42	6241	1	2	t
109502	417	50	41	6243	3	2	t
109453	417	49	42	6242	3	2	f
109504	417	50	43	6243	3	0	t
109454	417	49	43	6242	3	1	f
109505	417	50	44	6243	0	2	f
109506	417	50	45	6243	0	2	t
109455	417	49	44	6242	3	2	f
109456	417	49	45	6242	3	0	f
109424	417	49	13	6242	3	2	f
109525	417	51	14	6244	0	1	t
109412	417	49	1	6242	0	2	t
109513	417	51	2	6244	3	1	t
109526	417	51	15	6244	1	2	t
109514	417	51	3	6244	1	2	t
109413	417	49	2	6242	3	1	t
109415	417	49	4	6242	3	2	t
109475	417	50	14	6243	3	1	f
109416	417	49	5	6242	3	1	f
109515	417	51	4	6244	3	2	f
109517	417	51	6	6244	3	0	t
109516	417	51	5	6244	3	1	f
109417	417	49	6	6242	3	2	t
109518	417	51	7	6244	0	2	f
109507	417	50	46	6243	3	2	t
109418	417	49	7	6242	3	1	f
109427	417	49	16	6242	1	2	t
109406	417	48	45	6241	1	2	t
109476	417	50	15	6243	3	2	t
109477	417	50	16	6243	3	2	f
109478	417	50	17	6243	3	1	f
109428	417	49	17	6242	3	2	t
109429	417	49	18	6242	3	0	t
109529	417	51	18	6244	3	1	f
109430	417	49	19	6242	0	3	f
109530	417	51	19	6244	3	2	f
109431	417	49	20	6242	0	2	t
109533	417	51	22	6244	0	1	t
109481	417	50	20	6243	0	3	t
109432	417	49	21	6242	3	2	f
109482	417	50	21	6243	3	2	f
109458	417	49	47	6242	3	0	f
109534	417	51	23	6244	1	3	t
109483	417	50	22	6243	3	2	f
109435	417	49	24	6242	1	2	t
109484	417	50	23	6243	3	1	f
109457	417	49	46	6242	3	2	f
109436	417	49	25	6242	3	2	t
109485	417	50	24	6243	3	2	t
109487	417	50	26	6243	3	0	t
109486	417	50	25	6243	3	2	f
109538	417	51	27	6244	0	1	t
109387	417	48	26	6241	3	1	t
109488	417	50	27	6243	0	2	f
109489	417	50	28	6243	0	1	t
109408	417	48	47	6241	3	1	f
109539	417	51	28	6244	1	2	t
109441	417	49	30	6242	0	2	t
109439	417	49	28	6242	1	2	t
109490	417	50	29	6243	1	2	t
109540	417	51	29	6244	3	2	t
109391	417	48	30	6241	3	0	t
109409	417	48	48	6241	3	2	f
109541	417	51	30	6244	3	0	t
109459	417	49	48	6242	3	2	f
109410	417	48	49	6241	3	0	t
109460	417	49	49	6242	3	1	f
109510	417	50	49	6243	3	2	f
109569	417	52	8	6245	0	2	f
109669	417	54	8	6247	0	3	t
109570	417	52	9	6245	0	2	f
109571	417	52	10	6245	0	1	t
109670	417	54	9	6247	3	1	f
109592	417	52	31	6245	0	1	t
109593	417	52	32	6245	1	2	t
109692	417	54	31	6247	3	2	t
109594	417	52	33	6245	3	0	t
109543	417	51	32	6244	1	2	t
108393	417	28	32	6221	2	1	f
109595	417	52	34	6245	0	1	t
109544	417	51	33	6244	3	2	f
109646	417	53	35	6246	0	2	t
109645	417	53	34	6246	0	3	f
109545	417	51	34	6244	3	1	f
109621	417	53	10	6246	0	3	t
109622	417	53	11	6246	3	0	t
109623	417	53	12	6246	0	2	f
109572	417	52	11	6245	1	2	t
109596	417	52	35	6245	1	2	t
109597	417	52	36	6245	3	0	t
109548	417	51	37	6244	0	1	t
109697	417	54	36	6247	3	0	t
109547	417	51	36	6244	3	0	t
109598	417	52	37	6245	0	1	t
109649	417	53	38	6246	3	0	t
109698	417	54	37	6247	0	2	t
109599	417	52	38	6245	1	2	t
109650	417	53	39	6246	0	1	t
109549	417	51	38	6244	1	2	t
109574	417	52	13	6245	3	0	t
109573	417	52	12	6245	3	2	f
109673	417	54	12	6247	3	2	f
109624	417	53	13	6246	0	3	t
109575	417	52	14	6245	0	2	f
109600	417	52	39	6245	3	0	t
109601	417	52	40	6245	0	1	t
109550	417	51	39	6244	3	1	f
109652	417	53	41	6246	0	3	f
109651	417	53	40	6246	1	0	t
109551	417	51	40	6244	3	0	f
109603	417	52	42	6245	3	0	t
109602	417	52	41	6245	1	2	t
109653	417	53	42	6246	0	3	t
109604	417	52	43	6245	0	1	t
109655	417	53	44	6246	3	0	t
109654	417	53	43	6246	3	1	f
109612	417	53	1	6246	3	2	f
109563	417	52	2	6245	3	0	t
109675	417	54	14	6247	3	0	t
109613	417	53	2	6246	3	0	t
109665	417	54	4	6247	0	1	f
109564	417	52	3	6245	0	3	t
109576	417	52	15	6245	0	2	t
109615	417	53	4	6246	0	2	f
109616	417	53	5	6246	0	3	t
109617	417	53	6	6246	3	1	f
109666	417	54	5	6247	0	3	t
109618	417	53	7	6246	3	0	t
109667	417	54	6	6247	3	2	f
109668	417	54	7	6247	3	0	t
109676	417	54	15	6247	0	2	t
109627	417	53	16	6246	0	3	t
109656	417	53	45	6246	0	2	f
109577	417	52	16	6245	3	2	f
109628	417	53	17	6246	3	0	t
109578	417	52	17	6245	3	2	f
109629	417	53	18	6246	0	1	f
109680	417	54	19	6247	3	0	t
109679	417	54	18	6247	0	2	t
109605	417	52	44	6245	1	2	t
109630	417	53	19	6246	0	3	t
109681	417	54	20	6247	0	3	t
109682	417	54	21	6247	3	0	t
109631	417	53	20	6246	3	0	t
109632	417	53	21	6246	0	3	t
109583	417	52	22	6245	0	1	t
109685	417	54	24	6247	0	2	t
109683	417	54	22	6247	0	2	t
109684	417	54	23	6247	3	0	t
109555	417	51	44	6244	1	2	t
109584	417	52	23	6245	1	2	t
109585	417	52	24	6245	3	0	t
109586	417	52	25	6245	0	1	t
109686	417	54	25	6247	3	0	t
109637	417	53	26	6246	0	2	t
109687	417	54	26	6247	0	2	t
109688	417	54	27	6247	3	0	t
109607	417	52	46	6245	0	1	t
109589	417	52	28	6245	0	1	t
109638	417	53	27	6246	3	2	f
109689	417	54	28	6247	0	2	t
109690	417	54	29	6247	3	0	t
109590	417	52	29	6245	1	2	t
109691	417	54	30	6247	0	2	t
109606	417	52	45	6245	3	0	t
109591	417	52	30	6245	3	0	t
109657	417	53	46	6246	0	2	t
109608	417	52	47	6245	1	2	t
109559	417	51	48	6244	0	1	t
109658	417	53	47	6246	3	2	f
109610	417	52	49	6245	0	1	t
109609	417	52	48	6245	3	0	t
109560	417	51	49	6244	1	2	t
109819	417	57	8	6250	0	2	f
109820	417	57	9	6250	0	1	t
109719	417	55	8	6248	3	0	t
109821	417	57	10	6250	1	2	t
109720	417	55	9	6248	0	3	t
109842	417	57	31	6250	1	2	t
109792	417	56	31	6249	3	2	f
109843	417	57	32	6250	3	1	f
108394	417	28	33	6221	2	0	t
108994	417	40	33	6233	3	0	t
109844	417	57	33	6250	3	0	t
109845	417	57	34	6250	0	1	t
109745	417	55	34	6248	3	1	f
109746	417	55	35	6248	3	0	t
109822	417	57	11	6250	3	0	t
109721	417	55	10	6248	3	1	f
109722	417	55	11	6248	3	2	f
109823	417	57	12	6250	0	1	t
109747	417	55	36	6248	0	1	t
109846	417	57	35	6250	1	2	t
109796	417	56	35	6249	3	2	f
109847	417	57	36	6250	3	0	t
109848	417	57	37	6250	0	1	t
109849	417	57	38	6250	1	2	t
109748	417	55	37	6248	1	3	t
109749	417	55	38	6248	3	1	t
109850	417	57	39	6250	3	0	t
109699	417	54	38	6247	3	2	f
109723	417	55	12	6248	3	2	t
109824	417	57	13	6250	1	2	t
109773	417	56	12	6249	3	2	f
109724	417	55	13	6248	3	2	f
109825	417	57	14	6250	3	0	t
109750	417	55	39	6248	1	2	t
109800	417	56	39	6249	3	2	f
109851	417	57	40	6250	0	1	t
109751	417	55	40	6248	3	0	t
109702	417	54	41	6247	0	2	t
109801	417	56	40	6249	3	2	t
109752	417	55	41	6248	0	3	t
109703	417	54	42	6247	3	0	t
109852	417	57	41	6250	1	2	t
109753	417	55	42	6248	3	1	f
109704	417	54	43	6247	0	2	t
109853	417	57	42	6250	3	2	f
109812	417	57	1	6250	0	2	t
109813	417	57	2	6250	3	1	t
109713	417	55	2	6248	3	2	t
109814	417	57	3	6250	1	2	t
109715	417	55	4	6248	0	2	t
109725	417	55	14	6248	3	0	t
109815	417	57	4	6250	3	1	f
109816	417	57	5	6250	3	0	t
109717	417	55	6	6248	0	1	t
109716	417	55	5	6248	3	0	t
109726	417	55	15	6248	0	1	t
109817	417	57	6	6250	0	2	t
109818	417	57	7	6250	3	0	t
109718	417	55	7	6248	1	2	t
109854	417	57	43	6250	3	2	t
109827	417	57	16	6250	1	2	t
109826	417	57	15	6250	0	1	t
109754	417	55	43	6248	3	2	f
109828	417	57	17	6250	3	0	t
109727	417	55	16	6248	1	3	t
109728	417	55	17	6248	3	1	t
109705	417	54	44	6247	3	0	t
109829	417	57	18	6250	0	1	f
109830	417	57	19	6250	0	1	t
109729	417	55	18	6248	1	3	t
109730	417	55	19	6248	3	2	f
109831	417	57	20	6250	1	2	t
109832	417	57	21	6250	3	1	f
109781	417	56	20	6249	3	2	t
109833	417	57	22	6250	3	0	t
109782	417	56	21	6249	3	2	t
109834	417	57	23	6250	0	1	t
109783	417	56	22	6249	3	2	f
109835	417	57	24	6250	1	2	t
109784	417	56	23	6249	3	2	t
109735	417	55	24	6248	3	1	f
109836	417	57	25	6250	3	1	t
109755	417	55	44	6248	3	1	f
109736	417	55	25	6248	3	2	t
109837	417	57	26	6250	1	2	t
109737	417	55	26	6248	3	1	f
109738	417	55	27	6248	3	1	f
109739	417	55	28	6248	3	1	f
109838	417	57	27	6250	3	2	t
109706	417	54	45	6247	0	2	t
109839	417	57	28	6250	3	2	f
109840	417	57	29	6250	3	0	t
109740	417	55	29	6248	3	2	t
109841	417	57	30	6250	0	1	t
109805	417	56	44	6249	3	2	f
109791	417	56	30	6249	3	2	f
109756	417	55	45	6248	3	2	t
109707	417	54	46	6247	3	0	t
109708	417	54	47	6247	0	2	t
109807	417	56	46	6249	3	2	f
109709	417	54	48	6247	3	0	t
109808	417	56	47	6249	3	2	f
109759	417	55	48	6248	3	1	f
109710	417	54	49	6247	0	2	t
109760	417	55	49	6248	3	1	f
109919	417	59	8	6252	3	0	t
109869	417	58	8	6251	3	2	t
109942	417	59	31	6252	0	2	t
109920	417	59	9	6252	0	2	f
109120	417	43	9	6236	3	2	f
109943	417	59	32	6252	3	0	t
109895	417	58	34	6251	3	0	t
109893	417	58	32	6251	0	3	f
109944	417	59	33	6252	0	2	t
109896	417	58	35	6251	0	2	t
109945	417	59	34	6252	3	2	f
109897	417	58	36	6251	3	1	f
109898	417	58	37	6251	3	2	t
109947	417	59	36	6252	3	2	t
109899	417	58	38	6251	3	2	f
109949	417	59	38	6252	3	2	f
109870	417	58	9	6251	3	2	f
109921	417	59	10	6252	0	2	f
109900	417	58	39	6251	3	2	f
109901	417	58	40	6251	3	0	t
109902	417	58	41	6251	0	2	f
109951	417	59	40	6252	3	0	f
109903	417	58	42	6251	0	1	t
109953	417	59	42	6252	3	2	f
109904	417	58	43	6251	1	2	t
109955	417	59	44	6252	0	2	t
109905	417	58	44	6251	3	0	t
109956	417	59	45	6252	3	0	t
109957	417	59	46	6252	0	2	t
109471	417	50	10	6243	3	0	t
109871	417	58	10	6251	3	0	t
109872	417	58	11	6251	0	1	t
107871	417	18	10	6211	3	1	f
108321	417	27	10	6220	3	1	f
109121	417	43	10	6236	3	2	t
109873	417	58	12	6251	1	0	t
109922	417	59	11	6252	0	2	t
109874	417	58	13	6251	0	2	t
109923	417	59	12	6252	3	1	t
109925	417	59	14	6252	3	1	t
107661	417	14	0	6207	1	0	t
107761	417	16	0	6209	1	0	f
107611	417	13	0	6206	1	0	f
108624	417	33	13	6226	3	0	t
107811	417	17	0	6210	1	0	f
109924	417	59	13	6252	1	2	t
107561	417	12	0	6205	1	0	f
108474	417	30	13	6223	3	1	f
108811	417	37	0	6230	2	0	f
108111	417	23	0	6216	2	0	f
108461	417	30	0	6223	2	0	f
109161	417	44	0	6237	3	0	t
107311	417	7	0	6200	0	3	t
109261	417	46	0	6239	3	0	t
109411	417	49	0	6242	3	0	t
107361	417	8	0	6201	0	3	t
109674	417	54	13	6247	3	1	f
109311	417	47	0	6240	3	0	t
107812	417	17	1	6210	1	0	t
107562	417	12	1	6205	1	0	t
107362	417	8	1	6201	0	3	t
107462	417	10	1	6203	1	2	t
107612	417	13	1	6206	1	2	t
109865	417	58	4	6251	3	2	f
109863	417	58	2	6251	3	2	t
109913	417	59	2	6252	3	0	f
109914	417	59	3	6252	3	0	t
109866	417	58	5	6251	3	2	f
109864	417	58	3	6251	3	2	t
109915	417	59	4	6252	0	2	t
109916	417	59	5	6252	3	0	t
109867	417	58	6	6251	3	2	f
109917	417	59	6	6252	0	2	f
109918	417	59	7	6252	0	2	t
107874	417	18	13	6211	3	1	f
109868	417	58	7	6251	3	2	t
109875	417	58	14	6251	3	2	t
109926	417	59	15	6252	1	2	t
109876	417	58	15	6251	3	2	t
109927	417	59	16	6252	3	1	f
109928	417	59	17	6252	3	1	f
109877	417	58	16	6251	3	2	f
109929	417	59	18	6252	3	1	f
109930	417	59	19	6252	3	2	t
109879	417	58	18	6251	3	2	f
109857	417	57	46	6250	1	2	t
109931	417	59	20	6252	3	2	t
109883	417	58	22	6251	3	0	t
109932	417	59	21	6252	3	2	t
109884	417	58	23	6251	0	1	t
109933	417	59	22	6252	3	2	f
109885	417	58	24	6251	1	0	f
109858	417	57	47	6250	3	0	t
109935	417	59	24	6252	3	1	f
109886	417	58	25	6251	1	3	f
109937	417	59	26	6252	0	2	t
109938	417	59	27	6252	3	0	t
109939	417	59	28	6252	0	2	t
109940	417	59	29	6252	3	2	f
109889	417	58	28	6251	3	2	t
109941	417	59	30	6252	3	0	t
109891	417	58	30	6251	3	2	f
109958	417	59	47	6252	3	0	t
109859	417	57	48	6250	0	2	t
109960	417	59	49	6252	0	2	t
109959	417	59	48	6252	0	2	f
109860	417	57	49	6250	3	1	f
107111	417	3	0	6196	0	3	t
108693	417	34	32	6227	3	1	f
109811	417	57	0	6250	3	0	t
107061	417	2	0	6195	0	3	t
107621	417	13	10	6206	1	0	t
107261	417	6	0	6199	0	3	f
107211	417	5	0	6198	0	3	f
107471	417	10	10	6203	2	0	t
107161	417	4	0	6197	0	3	f
107721	417	15	10	6208	2	0	t
107411	417	9	0	6202	0	3	f
107771	417	16	10	6209	1	2	t
107911	417	19	0	6212	1	2	t
108761	417	36	0	6229	2	1	t
108411	417	29	0	6222	2	1	f
108161	417	24	0	6217	2	1	f
108211	417	25	0	6218	2	1	f
108293	417	26	32	6219	3	1	f
108361	417	28	0	6221	2	1	f
108561	417	32	0	6225	2	1	f
108221	417	25	10	6218	2	1	f
108011	417	21	0	6214	2	1	f
109743	417	55	32	6248	3	1	f
107961	417	20	0	6213	2	1	f
108571	417	32	10	6225	2	1	f
108511	417	31	0	6224	2	1	f
107193	417	4	32	6197	2	3	t
108311	417	27	0	6220	2	1	f
109243	417	45	32	6238	3	2	t
108661	417	34	0	6227	2	1	f
108621	417	33	10	6226	3	1	f
108061	417	22	0	6215	2	1	f
108711	417	35	0	6228	2	1	f
108121	417	23	10	6216	3	1	f
109011	417	41	0	6234	3	1	t
107861	417	18	0	6211	1	3	t
107511	417	11	0	6204	1	3	f
108821	417	37	10	6230	3	1	f
107711	417	15	0	6208	1	3	f
109671	417	54	10	6247	3	1	f
108261	417	26	0	6219	2	3	t
109461	417	50	0	6243	3	2	t
108861	417	38	0	6231	2	3	t
109611	417	53	0	6246	3	2	t
108911	417	39	0	6232	2	3	t
109211	417	45	0	6238	3	2	t
107194	417	4	33	6197	0	3	t
108611	417	33	0	6226	2	3	t
109711	417	55	0	6248	3	2	t
109561	417	52	0	6245	3	2	f
109511	417	51	0	6244	3	2	f
109911	417	59	0	6252	3	2	f
109361	417	48	0	6241	3	2	f
108961	417	40	0	6233	3	2	f
107622	417	13	11	6206	1	0	t
109761	417	56	0	6249	3	2	f
109661	417	54	0	6247	3	2	f
109061	417	42	0	6235	3	2	f
109861	417	58	0	6251	3	2	f
109111	417	43	0	6236	3	2	f
107262	417	6	1	6199	0	1	t
107412	417	9	1	6202	0	1	t
107062	417	2	1	6195	0	1	t
107162	417	4	1	6197	0	1	t
107512	417	11	1	6204	1	0	f
108062	417	22	1	6215	2	0	t
108662	417	34	1	6227	2	0	t
108212	417	25	1	6218	2	0	t
107212	417	5	1	6198	0	2	t
108312	417	27	1	6220	2	0	t
109312	417	47	1	6240	0	2	t
108712	417	35	1	6228	2	0	t
108562	417	32	1	6225	2	0	f
109662	417	54	1	6247	3	0	t
107862	417	18	1	6211	3	0	t
108912	417	39	1	6232	3	0	t
109062	417	42	1	6235	3	0	t
108962	417	40	1	6233	3	0	f
109462	417	50	1	6243	3	0	f
109362	417	48	1	6241	3	0	f
107962	417	20	1	6213	2	1	t
107712	417	15	1	6208	1	2	t
108012	417	21	1	6214	2	1	t
108512	417	31	1	6224	2	1	f
108862	417	38	1	6231	3	1	t
109512	417	51	1	6244	3	1	f
108612	417	33	1	6226	3	1	f
109212	417	45	1	6238	3	1	f
109712	417	55	1	6248	3	1	f
109862	417	58	1	6251	3	2	t
108362	417	28	1	6221	2	3	t
108262	417	26	1	6219	3	2	t
109762	417	56	1	6249	3	2	f
109912	417	59	1	6252	3	2	f
109562	417	52	1	6245	3	2	f
109112	417	43	1	6236	3	2	f
109663	417	54	2	6247	0	3	t
108613	417	33	2	6226	3	0	f
107413	417	9	2	6202	1	2	t
107563	417	12	2	6205	1	2	t
108263	417	26	2	6219	2	1	f
108863	417	38	2	6231	2	1	f
108813	417	37	2	6230	2	1	f
108963	417	40	2	6233	3	1	t
107513	417	11	2	6204	1	3	t
107063	417	2	2	6195	1	3	f
108363	417	28	2	6221	3	2	t
107213	417	5	2	6198	2	3	t
109113	417	43	2	6236	3	2	t
107963	417	20	2	6213	2	3	t
107914	417	19	3	6212	1	0	t
107221	417	5	10	6198	2	3	t
109363	417	48	2	6241	3	2	t
107743	417	15	32	6208	2	3	t
109693	417	54	32	6247	3	2	t
109463	417	50	2	6243	3	2	t
107763	417	16	2	6209	2	3	t
109071	417	42	10	6235	3	2	f
108113	417	23	2	6216	2	3	t
109771	417	56	10	6249	3	2	f
109763	417	56	2	6249	3	2	t
108763	417	36	2	6229	2	3	t
109521	417	51	10	6244	3	2	f
108563	417	32	2	6225	2	3	t
109614	417	53	3	6246	0	1	f
108414	417	29	3	6222	0	1	f
109314	417	47	3	6240	0	2	t
107564	417	12	3	6205	2	0	t
107164	417	4	3	6197	0	2	t
108264	417	26	3	6219	2	0	t
107264	417	6	3	6199	0	3	t
109664	417	54	3	6247	3	0	t
107814	417	17	3	6210	3	0	t
109164	417	44	3	6237	3	0	t
107764	417	16	3	6209	3	0	t
109364	417	48	3	6241	3	0	t
107214	417	5	3	6198	0	3	t
109714	417	55	3	6248	3	0	t
109414	417	49	3	6242	1	2	t
108364	417	28	3	6221	2	1	t
108964	417	40	3	6233	1	2	t
108014	417	21	3	6214	2	1	t
107614	417	13	3	6206	1	2	f
108764	417	36	3	6229	3	1	t
108614	417	33	3	6226	3	1	t
108564	417	32	3	6225	3	1	t
107064	417	2	3	6195	1	3	t
107964	417	20	3	6213	3	1	t
108464	417	30	3	6223	3	1	f
108214	417	25	3	6218	3	1	f
108114	417	23	3	6216	3	1	f
107514	417	11	3	6204	3	2	t
108814	417	37	3	6230	2	3	t
107414	417	9	3	6202	2	3	t
109464	417	50	3	6243	3	2	t
109014	417	41	3	6234	3	2	f
109114	417	43	3	6236	3	2	f
109764	417	56	3	6249	3	2	f
107515	417	11	4	6204	2	0	t
107315	417	7	4	6200	0	3	t
108315	417	27	4	6220	3	0	t
107765	417	16	4	6209	1	2	t
108715	417	35	4	6228	2	1	f
107222	417	5	11	6198	0	3	t
108065	417	22	4	6215	2	1	f
109522	417	51	11	6244	3	2	t
107565	417	12	4	6205	1	3	t
108815	417	37	4	6230	3	1	t
109372	417	48	11	6241	3	2	f
109072	417	42	11	6235	3	2	f
107865	417	18	4	6211	3	1	f
109772	417	56	11	6249	3	2	f
107165	417	4	4	6197	2	3	t
109765	417	56	4	6249	3	2	t
109122	417	43	11	6236	3	2	f
108165	417	24	4	6217	2	3	t
109565	417	52	4	6245	3	2	t
107724	417	15	13	6208	1	2	t
109374	417	48	13	6241	3	1	f
108565	417	32	4	6225	2	3	t
109465	417	50	4	6243	3	2	f
109774	417	56	13	6249	3	2	f
109215	417	45	4	6238	3	2	f
108965	417	40	4	6233	3	2	f
109315	417	47	4	6240	3	2	f
107075	417	2	14	6195	0	3	t
107666	417	14	5	6207	1	0	t
107166	417	4	5	6197	0	1	f
108316	417	27	5	6220	0	1	f
108716	417	35	5	6228	2	0	f
109316	417	47	5	6240	3	0	t
107866	417	18	5	6211	3	0	t
107316	417	7	5	6200	0	3	f
107516	417	11	5	6204	1	2	t
108066	417	22	5	6215	2	1	t
108816	417	37	5	6230	2	1	f
108566	417	32	5	6225	3	1	t
107416	417	9	5	6202	1	3	t
109216	417	45	5	6238	3	1	t
109566	417	52	5	6245	3	1	f
108966	417	40	5	6233	3	1	f
108866	417	38	5	6231	3	1	f
108166	417	24	5	6217	3	1	f
109766	417	56	5	6249	3	2	t
107766	417	16	5	6209	2	3	t
109466	417	50	5	6243	3	2	t
107566	417	12	5	6205	3	2	f
107117	417	3	6	6196	0	3	t
107767	417	16	6	6209	3	0	t
107267	417	6	6	6199	0	3	t
107417	417	9	6	6202	0	3	t
107567	417	12	6	6205	3	0	f
108717	417	35	6	6228	2	1	f
108117	417	23	6	6216	2	1	f
109117	417	43	6	6236	3	1	f
108417	417	29	6	6222	3	1	f
107917	417	19	6	6212	2	3	t
108567	417	32	6	6225	2	3	t
108817	417	37	6	6230	2	3	t
109067	417	42	6	6235	3	2	t
109467	417	50	6	6243	3	2	f
109767	417	56	6	6249	3	2	f
109567	417	52	6	6245	3	2	f
108167	417	24	6	6217	3	2	f
109367	417	48	6	6241	3	2	f
107268	417	6	7	6199	0	1	t
108118	417	23	7	6216	2	0	t
107918	417	19	7	6212	3	0	t
107118	417	3	7	6196	0	3	t
109568	417	52	7	6245	3	0	t
107418	417	9	7	6202	0	3	t
107768	417	16	7	6209	1	2	t
108568	417	32	7	6225	3	1	t
107568	417	12	7	6205	3	1	t
108418	417	29	7	6222	3	1	t
108818	417	37	7	6230	3	1	t
108168	417	24	7	6217	3	1	f
109368	417	48	7	6241	3	2	t
109068	417	42	7	6235	3	2	t
109069	417	42	8	6235	3	2	f
108718	417	35	7	6228	2	3	t
109468	417	50	7	6243	3	2	t
108868	417	38	7	6231	2	3	t
109768	417	56	7	6249	3	2	f
109118	417	43	7	6236	3	2	f
108122	417	23	11	6216	3	0	t
107324	417	7	13	6200	0	1	t
107725	417	15	14	6208	2	0	t
107375	417	8	14	6201	0	3	t
106975	417	0	14	6193	0	3	t
109125	417	43	14	6236	3	0	t
108925	417	39	14	6232	2	1	f
108325	417	27	14	6220	2	1	f
108343	417	27	32	6220	2	3	t
108775	417	36	14	6229	2	1	f
109143	417	43	32	6236	3	2	t
108025	417	21	14	6214	2	1	f
108475	417	30	14	6223	3	1	f
107275	417	6	14	6199	2	3	t
108793	417	36	32	6229	2	3	t
109425	417	49	14	6242	3	2	t
109043	417	41	32	6234	3	2	t
109075	417	42	14	6235	3	2	t
107975	417	20	14	6213	2	3	t
109775	417	56	14	6249	3	2	t
108794	417	36	33	6229	3	1	f
108275	417	26	14	6219	2	3	t
109625	417	53	14	6246	3	2	t
109375	417	48	14	6241	3	2	f
107576	417	12	15	6205	1	0	t
108326	417	27	15	6220	2	0	t
107276	417	6	15	6199	0	3	t
107776	417	16	15	6209	3	0	t
108476	417	30	15	6223	3	0	t
109376	417	48	15	6241	3	0	t
109626	417	53	15	6246	3	0	t
107426	417	9	15	6202	0	3	f
108926	417	39	15	6232	2	1	f
108726	417	35	15	6228	2	1	f
109426	417	49	15	6242	3	1	t
108276	417	26	15	6219	3	1	f
107976	417	20	15	6213	3	1	f
108776	417	36	15	6229	2	3	t
109076	417	42	15	6235	3	2	t
108026	417	21	15	6214	2	3	t
109776	417	56	15	6249	3	2	t
107527	417	11	16	6204	1	0	t
107177	417	4	16	6197	0	1	t
107427	417	9	16	6202	0	1	f
108927	417	39	16	6232	2	0	f
107877	417	18	16	6211	3	0	t
107727	417	15	16	6208	3	0	t
107277	417	6	16	6199	0	3	f
108527	417	31	16	6224	2	1	t
108727	417	35	16	6228	2	1	t
108377	417	28	16	6221	3	1	t
108177	417	24	16	6217	3	1	t
107977	417	20	16	6213	3	1	f
108027	417	21	16	6214	3	1	f
109777	417	56	16	6249	3	2	f
109677	417	54	16	6247	3	2	f
109077	417	42	16	6235	3	2	f
109277	417	46	16	6239	3	2	f
109527	417	51	16	6244	3	2	f
107528	417	11	17	6204	1	0	t
107878	417	18	17	6211	1	0	f
109678	417	54	17	6247	3	0	t
107278	417	6	17	6199	0	3	t
109278	417	46	17	6239	3	0	t
107478	417	10	17	6203	3	0	f
109528	417	51	17	6244	3	0	f
108378	417	28	17	6221	2	1	t
108728	417	35	17	6228	2	1	f
108178	417	24	17	6217	2	1	f
108528	417	31	17	6224	2	1	f
107178	417	4	17	6197	1	3	t
108028	417	21	17	6214	3	1	f
108778	417	36	17	6229	3	1	f
109228	417	45	17	6238	3	1	f
107978	417	20	17	6213	3	1	f
107778	417	16	17	6209	2	3	t
109878	417	58	17	6251	3	2	t
108928	417	39	17	6232	2	3	t
109778	417	56	17	6249	3	2	f
109078	417	42	17	6235	3	2	f
107579	417	12	18	6205	1	0	t
108229	417	25	18	6218	3	0	t
107329	417	7	18	6200	0	3	t
107779	417	16	18	6209	3	0	t
107179	417	4	18	6197	0	3	t
107479	417	10	18	6203	3	0	t
108829	417	37	18	6230	2	1	f
108479	417	30	18	6223	2	1	f
108729	417	35	18	6228	2	1	f
108329	417	27	18	6220	2	1	f
107580	417	12	19	6205	1	0	t
108230	417	25	19	6218	0	1	t
108480	417	30	19	6223	2	0	f
108029	417	21	18	6214	3	1	t
109643	417	53	32	6246	3	2	f
108929	417	39	18	6232	3	1	f
107979	417	20	18	6213	3	1	f
109329	417	47	18	6240	3	2	t
109793	417	56	32	6249	3	2	f
109079	417	42	18	6235	3	2	t
109779	417	56	18	6249	3	2	f
109579	417	52	18	6245	3	2	f
109479	417	50	18	6243	3	2	f
109644	417	53	33	6246	3	0	t
109480	417	50	19	6243	3	0	t
109230	417	45	19	6238	3	0	t
107080	417	2	19	6195	0	3	f
109044	417	41	33	6234	3	0	t
107330	417	7	19	6200	0	3	f
108030	417	21	19	6214	2	1	f
108330	417	27	19	6220	2	1	f
108730	417	35	19	6228	2	1	f
107980	417	20	19	6213	3	1	t
109580	417	52	19	6245	3	1	t
107780	417	16	19	6209	1	3	t
107430	417	9	19	6202	2	3	t
108830	417	37	19	6230	2	3	t
107880	417	18	19	6211	3	2	f
109030	417	41	19	6234	3	2	f
108344	417	27	33	6220	3	1	f
109880	417	58	19	6251	3	2	f
109780	417	56	19	6249	3	2	f
109330	417	47	19	6240	3	2	f
109244	417	45	33	6238	3	2	t
107431	417	9	20	6202	0	1	t
109331	417	47	20	6240	3	0	t
109744	417	55	33	6248	3	2	f
107781	417	16	20	6209	3	0	t
107081	417	2	20	6195	0	3	t
109031	417	41	20	6234	3	0	t
107331	417	7	20	6200	0	3	f
109794	417	56	33	6249	3	2	f
107531	417	11	20	6204	1	2	t
109581	417	52	20	6245	1	2	t
108081	417	22	20	6215	2	1	t
108431	417	29	20	6222	2	1	f
108795	417	36	34	6229	3	0	t
108731	417	35	20	6228	2	1	f
107445	417	9	34	6202	0	3	t
108531	417	31	20	6224	2	1	f
108695	417	34	34	6227	3	0	t
108831	417	37	20	6230	3	1	t
108281	417	26	20	6219	2	3	t
109531	417	51	20	6244	3	2	f
109081	417	42	20	6235	3	2	f
109881	417	58	20	6251	3	2	f
109731	417	55	20	6248	3	2	f
107882	417	18	21	6211	1	0	t
108732	417	35	21	6228	2	0	t
107532	417	11	21	6204	2	0	t
109332	417	47	21	6240	0	2	f
109282	417	46	21	6239	3	0	t
107932	417	19	21	6212	3	0	t
107132	417	3	21	6196	0	3	t
109582	417	52	21	6245	3	0	t
107332	417	7	21	6200	0	3	t
109532	417	51	21	6244	3	0	t
108632	417	33	21	6226	2	1	t
107732	417	15	21	6208	1	2	t
108082	417	22	21	6215	2	1	t
108532	417	31	21	6224	2	1	f
108432	417	29	21	6222	2	1	f
107432	417	9	21	6202	1	3	t
109732	417	55	21	6248	3	1	f
109882	417	58	21	6251	3	2	t
108832	417	37	21	6230	2	3	t
109082	417	42	21	6235	3	2	f
108282	417	26	21	6219	3	2	f
108982	417	40	21	6233	3	2	f
107633	417	13	22	6206	1	0	t
107733	417	15	22	6208	2	0	t
107433	417	9	22	6202	0	2	t
109633	417	53	22	6246	3	0	t
107283	417	6	22	6199	0	3	t
108983	417	40	22	6233	3	0	t
107133	417	3	22	6196	0	3	t
107983	417	20	22	6213	2	1	f
108683	417	34	22	6227	2	1	f
108533	417	31	22	6224	2	1	f
108883	417	38	22	6231	3	1	f
108383	417	28	22	6221	3	1	f
108283	417	26	22	6219	3	1	f
109383	417	48	22	6241	3	2	t
109233	417	45	22	6238	3	2	t
109083	417	42	22	6235	3	2	f
109433	417	49	22	6242	3	2	f
109733	417	55	22	6248	3	2	f
107834	417	17	23	6210	1	0	t
109634	417	53	23	6246	0	1	t
107634	417	13	23	6206	1	0	f
107984	417	20	23	6213	2	0	t
107284	417	6	23	6199	0	3	t
109234	417	45	23	6238	3	0	t
107134	417	3	23	6196	0	3	f
107734	417	15	23	6208	1	2	t
108534	417	31	23	6224	2	1	t
108084	417	22	23	6215	2	1	f
108734	417	35	23	6228	2	1	f
109434	417	49	23	6242	3	1	t
108735	417	35	24	6228	2	0	t
107735	417	15	24	6208	2	0	t
106985	417	0	24	6193	0	2	t
107135	417	3	24	6196	0	3	t
108384	417	28	23	6221	3	1	f
108284	417	26	23	6219	3	1	f
108884	417	38	23	6231	3	1	f
107434	417	9	23	6202	2	3	t
109734	417	55	23	6248	3	2	t
108934	417	39	23	6232	2	3	t
109384	417	48	23	6241	3	2	t
108694	417	34	33	6227	3	1	f
108834	417	37	23	6230	2	3	t
109934	417	59	23	6252	3	2	f
109084	417	42	23	6235	3	2	f
107585	417	12	24	6205	1	0	f
109694	417	54	33	6247	3	2	f
107885	417	18	24	6211	1	0	f
109494	417	50	33	6243	3	2	f
109085	417	42	24	6235	3	0	t
107285	417	6	24	6199	0	3	f
107435	417	9	24	6202	0	3	f
108085	417	22	24	6215	2	1	t
108035	417	21	24	6214	2	1	f
109635	417	53	24	6246	1	3	t
108485	417	30	24	6223	3	1	t
108845	417	37	34	6230	2	1	f
109495	417	50	34	6243	3	1	t
108935	417	39	24	6232	3	1	f
108185	417	24	24	6217	2	3	t
109795	417	56	34	6249	3	2	f
109785	417	56	24	6249	3	2	f
109535	417	51	24	6244	3	2	f
108746	417	35	35	6228	2	1	t
108385	417	28	24	6221	3	2	f
109385	417	48	24	6241	3	2	f
108885	417	38	24	6231	3	2	f
107586	417	12	25	6205	1	0	t
108386	417	28	25	6221	3	0	t
109636	417	53	25	6246	3	0	t
107286	417	6	25	6199	0	3	t
109936	417	59	25	6252	3	0	t
108686	417	34	25	6227	2	1	f
107797	417	16	36	6209	1	2	t
108486	417	30	25	6223	2	1	f
108836	417	37	25	6230	3	1	t
107386	417	8	25	6201	1	3	t
109036	417	41	25	6234	3	1	t
108186	417	24	25	6217	3	1	t
107886	417	18	25	6211	1	3	t
107186	417	4	25	6197	1	3	f
106986	417	0	25	6193	2	3	t
107786	417	16	25	6209	2	3	t
108086	417	22	25	6215	2	3	t
108036	417	21	25	6214	2	3	t
109386	417	48	25	6241	3	2	f
109536	417	51	25	6244	3	2	f
109786	417	56	25	6249	3	2	f
109186	417	44	25	6237	3	2	f
107537	417	11	26	6204	1	0	t
107337	417	7	26	6200	0	3	t
109187	417	44	26	6237	3	0	t
107787	417	16	26	6209	3	0	t
109537	417	51	26	6244	3	0	t
107387	417	8	26	6201	0	3	t
109587	417	52	26	6245	1	2	t
108187	417	24	26	6217	2	1	t
109887	417	58	26	6251	1	2	t
109037	417	41	26	6234	1	2	t
108837	417	37	26	6230	2	1	t
108687	417	34	26	6227	2	1	f
108437	417	29	26	6222	2	1	f
108587	417	32	26	6225	2	1	f
107187	417	4	26	6197	1	3	t
107887	417	18	26	6211	3	1	f
108087	417	22	26	6215	3	1	f
109787	417	56	26	6249	3	2	t
109437	417	49	26	6242	3	2	f
107538	417	11	27	6204	1	0	t
109238	417	45	27	6238	0	2	f
107888	417	18	27	6211	3	0	t
107038	417	1	27	6194	0	3	t
109588	417	52	27	6245	3	0	t
107338	417	7	27	6200	0	3	t
107088	417	2	27	6195	0	3	f
108438	417	29	27	6222	2	1	t
107738	417	15	27	6208	1	2	t
108588	417	32	27	6225	2	1	t
107488	417	10	27	6203	1	3	t
109438	417	49	27	6242	3	1	t
109388	417	48	27	6241	1	3	t
108088	417	22	27	6215	3	1	t
108638	417	33	27	6226	2	3	t
109038	417	41	27	6234	3	2	t
108188	417	24	27	6217	2	3	t
109788	417	56	27	6249	3	2	f
108888	417	38	27	6231	3	2	f
109138	417	43	27	6236	3	2	f
109888	417	58	27	6251	3	2	f
107589	417	12	28	6205	1	0	t
107739	417	15	28	6208	2	0	t
107039	417	1	28	6194	0	3	t
109639	417	53	28	6246	3	0	t
107489	417	10	28	6203	3	0	t
107089	417	2	28	6195	0	3	f
107239	417	5	28	6198	0	3	f
108439	417	29	28	6222	2	1	t
108589	417	32	28	6225	2	1	f
107889	417	18	28	6211	1	3	t
108889	417	38	28	6231	3	1	t
108639	417	33	28	6226	3	1	f
107590	417	12	29	6205	1	0	t
109640	417	53	29	6246	0	2	f
107240	417	5	29	6198	0	3	t
107890	417	18	29	6211	3	0	t
109440	417	49	29	6242	3	0	t
107040	417	1	29	6194	0	3	f
108189	417	24	28	6217	3	1	f
109542	417	51	31	6244	0	1	t
108289	417	26	28	6219	2	3	t
109139	417	43	28	6236	3	2	t
107542	417	11	31	6204	1	0	t
109039	417	41	28	6234	3	2	t
109389	417	48	28	6241	3	2	f
107292	417	6	31	6199	0	1	f
109339	417	47	28	6240	3	2	f
108142	417	23	31	6216	2	0	t
109789	417	56	28	6249	3	2	f
108592	417	32	31	6225	2	0	t
107140	417	3	29	6196	0	3	t
108392	417	28	31	6221	2	0	f
107740	417	15	29	6208	1	2	t
108590	417	32	29	6225	2	1	t
109892	417	58	31	6251	3	0	t
108890	417	38	29	6231	2	1	f
109292	417	46	31	6239	3	0	t
108440	417	29	29	6222	2	1	f
108090	417	22	29	6215	2	1	f
109340	417	47	29	6240	3	1	t
107490	417	10	29	6203	1	3	t
108290	417	26	29	6219	3	1	t
107042	417	1	31	6194	0	3	t
108190	417	24	29	6217	3	1	f
108690	417	34	29	6227	2	3	t
109492	417	50	31	6243	3	0	t
109140	417	43	29	6236	3	2	f
108042	417	21	31	6214	2	1	t
109040	417	41	29	6234	3	2	f
108192	417	24	31	6217	3	1	t
109790	417	56	29	6249	3	2	f
109390	417	48	29	6241	3	2	f
109890	417	58	29	6251	3	2	f
107541	417	11	30	6204	1	0	t
107892	417	18	31	6211	3	1	f
107741	417	15	30	6208	2	0	f
107141	417	3	30	6196	0	3	t
109742	417	55	31	6248	3	1	f
109642	417	53	31	6246	3	2	t
107491	417	10	30	6203	3	0	t
107291	417	6	30	6199	0	3	t
109041	417	41	30	6234	3	0	t
109641	417	53	30	6246	0	3	t
109144	417	43	33	6236	3	2	t
108391	417	28	30	6221	2	1	f
107145	417	3	34	6196	0	3	t
108591	417	32	30	6225	2	1	f
108891	417	38	30	6231	2	1	f
108041	417	21	30	6214	3	1	t
107891	417	18	30	6211	1	3	t
108691	417	34	30	6227	3	1	t
108191	417	24	30	6217	3	1	f
109291	417	46	30	6239	3	2	f
108745	417	35	34	6228	2	1	f
109741	417	55	30	6248	3	2	f
109491	417	50	30	6243	3	2	f
109141	417	43	30	6236	3	2	f
108345	417	27	34	6220	3	1	f
107795	417	16	34	6209	2	3	t
109695	417	54	34	6247	3	2	t
109145	417	43	34	6236	3	2	f
107546	417	11	35	6204	2	0	t
107896	417	18	35	6211	3	0	t
108346	417	27	35	6220	3	0	t
107146	417	3	35	6196	0	3	t
107346	417	7	35	6200	0	3	t
109346	417	47	35	6240	3	0	f
108446	417	29	35	6222	2	1	t
108946	417	39	35	6232	2	1	f
108596	417	32	35	6225	3	1	t
108096	417	22	35	6215	3	1	f
109146	417	43	35	6236	3	2	t
109946	417	59	35	6252	3	2	f
109546	417	51	35	6244	3	2	f
109696	417	54	35	6247	3	2	f
107597	417	12	36	6205	1	0	f
107197	417	4	36	6197	0	2	f
107947	417	19	36	6212	3	0	t
107447	417	9	36	6202	0	3	t
107347	417	7	36	6200	0	3	t
107147	417	3	36	6196	0	3	f
109447	417	49	36	6242	1	2	t
108897	417	38	36	6231	2	1	f
108747	417	35	36	6228	2	1	f
108197	417	24	36	6217	3	1	t
109047	417	41	36	6234	3	1	f
109297	417	46	36	6239	3	1	f
108047	417	21	36	6214	2	3	t
108447	417	29	36	6222	2	3	t
109147	417	43	36	6236	3	2	t
108597	417	32	36	6225	2	3	t
109797	417	56	36	6249	3	2	t
109647	417	53	36	6246	3	2	f
107948	417	19	37	6212	1	0	t
107598	417	12	37	6205	1	0	t
107398	417	8	37	6201	0	3	t
107348	417	7	37	6200	0	3	t
109048	417	41	37	6234	3	0	t
109298	417	46	37	6239	3	0	t
107148	417	3	37	6196	0	3	f
107399	417	8	38	6201	0	3	t
107099	417	2	38	6195	0	3	t
108598	417	32	37	6225	3	1	t
108448	417	29	37	6222	3	1	f
108048	417	21	37	6214	3	1	f
109798	417	56	37	6249	3	2	t
109648	417	53	37	6246	3	2	f
109948	417	59	37	6252	3	2	f
107799	417	16	38	6209	3	0	t
108749	417	35	38	6228	2	1	t
108799	417	36	38	6229	3	1	f
108199	417	24	38	6217	3	1	f
108299	417	26	38	6219	2	3	t
109099	417	42	38	6235	3	2	t
109799	417	56	38	6249	3	2	f
109399	417	48	38	6241	3	2	f
107650	417	13	39	6206	1	0	t
107050	417	1	39	6194	0	3	t
109350	417	47	39	6240	3	0	t
107250	417	5	39	6198	0	3	f
108950	417	39	39	6232	2	1	t
108750	417	35	39	6228	2	1	f
108500	417	30	39	6223	3	1	t
108200	417	24	39	6217	3	1	t
107900	417	18	39	6211	1	3	t
108800	417	36	39	6229	3	1	t
108050	417	21	39	6214	3	1	f
109500	417	50	39	6243	3	1	f
108300	417	26	39	6219	3	1	f
107750	417	15	39	6208	2	3	t
109950	417	59	39	6252	3	2	f
109700	417	54	39	6247	3	2	f
109100	417	42	39	6235	3	2	f
107601	417	12	40	6205	1	0	t
108751	417	35	40	6228	2	0	t
107201	417	4	40	6197	0	2	t
107901	417	18	40	6211	3	0	t
109101	417	42	40	6235	3	0	t
107301	417	6	40	6199	0	3	t
109701	417	54	40	6247	3	0	t
107451	417	9	40	6202	0	3	t
109251	417	45	40	6238	3	0	f
108451	417	29	40	6222	3	0	f
107751	417	15	40	6208	3	0	f
108801	417	36	40	6229	2	1	t
108201	417	24	40	6217	2	1	f
108951	417	39	40	6232	2	1	f
108051	417	21	40	6214	3	1	f
109501	417	50	40	6243	3	2	t
108601	417	32	40	6225	2	3	t
107902	417	18	41	6211	1	0	t
107602	417	12	41	6205	1	0	t
107402	417	8	41	6201	0	3	t
107052	417	1	41	6194	0	3	f
107302	417	6	41	6199	0	3	f
108952	417	39	41	6232	2	1	f
108602	417	32	41	6225	3	1	f
109252	417	45	41	6238	3	1	f
109952	417	59	41	6252	3	1	f
108052	417	21	41	6214	3	1	f
109552	417	51	41	6244	3	2	t
109802	417	56	41	6249	3	2	t
109553	417	51	42	6244	3	0	t
107753	417	15	42	6208	3	0	t
107403	417	8	42	6201	0	3	f
107253	417	5	42	6198	0	3	f
107303	417	6	42	6199	0	3	f
108703	417	34	42	6227	2	1	f
108353	417	27	42	6220	2	1	f
108453	417	29	42	6222	3	1	t
108203	417	24	42	6217	3	1	f
108903	417	38	42	6231	3	1	f
109153	417	43	42	6236	3	2	f
109503	417	50	42	6243	3	2	f
109803	417	56	42	6249	3	2	f
109554	417	51	43	6244	0	1	t
107904	417	18	43	6211	1	0	t
107554	417	11	43	6204	2	0	f
107304	417	6	43	6199	0	3	t
109954	417	59	43	6252	3	0	t
109254	417	45	43	6238	3	0	t
107154	417	3	43	6196	0	3	f
108804	417	36	43	6229	2	1	t
108754	417	35	43	6228	2	1	f
108204	417	24	43	6217	3	1	f
108604	417	32	43	6225	3	1	f
108004	417	20	43	6213	3	1	f
107804	417	16	43	6209	2	3	t
109404	417	48	43	6241	3	2	t
109104	417	42	43	6235	3	2	f
109804	417	56	43	6249	3	2	f
109054	417	41	43	6234	3	2	f
107855	417	17	44	6210	1	0	f
107555	417	11	44	6204	2	0	t
109305	417	46	44	6239	0	2	t
108755	417	35	44	6228	2	0	t
108805	417	36	44	6229	2	0	t
107805	417	16	44	6209	3	0	t
107005	417	0	44	6193	0	3	f
107856	417	17	45	6210	1	0	t
107556	417	11	45	6204	1	0	f
109906	417	58	45	6251	0	2	t
109306	417	46	45	6239	3	0	t
107455	417	9	44	6202	0	3	f
108955	417	39	44	6232	2	1	t
107205	417	4	44	6197	1	3	t
109405	417	48	44	6241	3	1	t
108005	417	20	44	6213	3	1	t
108605	417	32	44	6225	3	1	f
109855	417	57	44	6250	3	2	f
109105	417	42	44	6235	3	2	f
108405	417	28	44	6221	3	2	f
108205	417	24	44	6217	3	2	f
108956	417	39	45	6232	2	0	t
107206	417	4	45	6197	0	2	f
108606	417	32	45	6225	3	0	t
107156	417	3	45	6196	0	3	t
108006	417	20	45	6213	2	1	f
108656	417	33	45	6226	2	1	f
107506	417	10	45	6203	1	3	t
109856	417	57	45	6250	3	1	t
108306	417	26	45	6219	2	3	t
109556	417	51	45	6244	3	2	t
109806	417	56	45	6249	3	2	f
108657	417	33	46	6226	2	0	t
107507	417	10	46	6203	3	0	t
107057	417	1	46	6194	0	3	f
107257	417	5	46	6198	0	3	f
108207	417	24	46	6217	3	1	t
108307	417	26	46	6219	3	1	f
108907	417	38	46	6231	3	1	f
109557	417	51	46	6244	3	1	f
107807	417	16	46	6209	2	3	t
109157	417	43	46	6236	3	2	f
109407	417	48	46	6241	3	2	f
109757	417	55	46	6248	3	2	f
109907	417	58	46	6251	3	2	f
107208	417	4	47	6197	0	1	t
107608	417	12	47	6205	1	0	t
108208	417	24	47	6217	2	0	t
109058	417	41	47	6234	3	0	t
109558	417	51	47	6244	3	0	t
107908	417	18	47	6211	3	0	t
107408	417	8	47	6201	0	3	t
107058	417	1	47	6194	0	3	t
107258	417	5	47	6198	0	3	t
108308	417	26	47	6219	3	0	f
107758	417	15	47	6208	1	2	t
109358	417	47	47	6240	1	2	t
108708	417	34	47	6227	2	1	t
108508	417	30	47	6223	3	1	f
108008	417	20	47	6213	2	3	t
109908	417	58	47	6251	3	2	t
109758	417	55	47	6248	3	2	f
108908	417	38	47	6231	3	2	f
109508	417	50	47	6243	3	2	f
109108	417	42	47	6235	3	2	f
107909	417	18	48	6211	1	0	f
107609	417	12	48	6205	1	0	f
107759	417	15	48	6208	2	0	t
108209	417	24	48	6217	0	2	f
109909	417	58	48	6251	3	0	t
108959	417	39	48	6232	0	3	f
107059	417	1	48	6194	0	3	f
107409	417	8	48	6201	0	3	f
108759	417	35	48	6228	2	1	f
108309	417	26	48	6219	3	1	t
107009	417	0	48	6193	1	3	t
108509	417	30	48	6223	3	1	t
109509	417	50	48	6243	3	1	f
108909	417	38	48	6231	3	2	t
108109	417	22	48	6215	2	3	t
109809	417	56	48	6249	3	2	t
109109	417	42	48	6235	3	2	t
109359	417	47	48	6240	3	2	f
109659	417	53	48	6246	3	2	f
109910	417	58	49	6251	0	1	t
107610	417	12	49	6205	1	0	t
108960	417	39	49	6232	0	2	t
108660	417	33	49	6226	2	0	t
107410	417	8	49	6201	0	3	t
107060	417	1	49	6194	0	3	f
108510	417	30	49	6223	2	1	t
107910	417	18	49	6211	1	3	t
109660	417	53	49	6246	3	1	f
108110	417	22	49	6215	3	1	f
109360	417	47	49	6240	3	2	t
109810	417	56	49	6249	3	2	f
\.


--
-- Data for Name: game_floatparameter; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.game_floatparameter (id, name, value) FROM stdin;
\.


--
-- Data for Name: game_intparameter; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.game_intparameter (id, name, value) FROM stdin;
12	timeOut	30000
13	reconnectTime	1000
14	delayRequest	1000
\.


--
-- Data for Name: game_probaexchangetraining; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.game_probaexchangetraining (id, desired_good, good_in_hand, p_success) FROM stdin;
1	1	0	0.400000000000000022
4	2	0	0.800000000000000044
5	3	0	0.800000000000000044
9	0	2	0.5
10	1	2	0.800000000000000044
11	3	2	0.5
12	0	3	0.5
13	1	3	0.800000000000000044
14	2	3	0.5
\.


--
-- Data for Name: game_room; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.game_room (id, n_user, t, t_max, tutorial_t, tutorial_t_max, trial, state, n_type, types, training_t, training_t_max, opened, counter) FROM stdin;
415	40	49	50	\N	\N	f	end	4	10/10/10/10	0	10	f	40
414	36	49	50	\N	\N	f	end	3	9/9/18	0	10	f	36
417	60	49	50	\N	\N	f	end	4	10/10/20/20	0	10	f	60
416	30	49	50	\N	\N	f	end	3	10/10/10	0	10	f	30
\.


--
-- Data for Name: game_tutorialchoice; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.game_tutorialchoice (id, room_id, player_id, t, user_id, good_in_hand, desired_good, success) FROM stdin;
18053	414	12	0	6099	1	2	t
18052	414	11	9	6098	2	0	f
18004	414	7	1	6094	0	2	t
18086	414	15	3	6102	1	0	f
18055	414	12	2	6099	1	0	f
18083	414	15	0	6102	1	0	t
18073	414	14	0	6101	1	2	t
18063	414	13	0	6100	1	2	t
17934	414	0	1	6087	1	2	t
17963	414	3	0	6090	0	1	t
18056	414	12	3	6099	1	2	t
18043	414	11	0	6098	1	0	t
18084	414	15	1	6102	1	0	t
17935	414	0	2	6087	0	1	t
17944	414	1	1	6088	0	1	t
18062	414	12	9	6099	2	0	t
17946	414	1	3	6088	0	1	t
18044	414	11	1	6098	1	2	t
17993	414	6	0	6093	0	2	t
17955	414	2	2	6089	1	2	f
18085	414	15	2	6102	1	0	f
17936	414	0	3	6087	1	2	t
17994	414	6	1	6093	0	2	f
17962	414	2	9	6089	1	2	t
18032	414	9	9	6096	2	1	t
18045	414	11	2	6098	2	1	t
18060	414	12	7	6099	2	0	t
18077	414	14	4	6101	1	2	t
18064	414	13	1	6100	2	0	t
17937	414	0	4	6087	0	2	t
18033	414	10	0	6097	1	0	t
18023	414	9	0	6096	1	0	f
18061	414	12	8	6099	1	2	t
18003	414	7	0	6094	0	2	t
18002	414	6	9	6093	1	2	f
18076	414	14	3	6101	1	2	f
17938	414	0	5	6087	0	2	t
18022	414	8	9	6095	1	2	t
18039	414	10	6	6097	1	2	f
18046	414	11	3	6098	1	2	t
18065	414	13	2	6100	1	0	f
18034	414	10	1	6097	1	2	t
17939	414	0	6	6087	0	1	t
17996	414	6	3	6093	0	1	t
17948	414	1	5	6088	1	2	t
18047	414	11	4	6098	2	0	t
18013	414	8	0	6095	0	1	t
18027	414	9	4	6096	2	0	t
18066	414	13	3	6100	1	2	t
17952	414	1	9	6088	0	2	f
18048	414	11	5	6098	1	0	f
17997	414	6	4	6093	1	2	t
17965	414	3	2	6090	0	2	t
17992	414	5	9	6092	0	2	f
17951	414	1	8	6088	1	2	t
17941	414	0	8	6087	1	2	t
18035	414	10	2	6097	2	0	t
18049	414	11	6	6098	1	2	t
18082	414	14	9	6101	2	0	t
18067	414	13	4	6100	2	0	t
17966	414	3	3	6090	0	1	t
18080	414	14	7	6101	1	2	f
18050	414	11	7	6098	2	1	f
18006	414	7	3	6094	0	2	t
18081	414	14	8	6101	1	2	t
18041	414	10	8	6097	1	0	f
17967	414	3	4	6090	1	2	t
18036	414	10	3	6097	1	2	t
18068	414	13	5	6100	1	0	t
17958	414	2	5	6089	1	2	t
17968	414	3	5	6090	0	2	t
18007	414	7	4	6094	0	1	t
18037	414	10	4	6097	2	0	t
17973	414	4	0	6091	0	2	t
18012	414	7	9	6094	0	2	f
18069	414	13	6	6100	1	2	t
18000	414	6	7	6093	1	2	f
18038	414	10	5	6097	1	0	t
17960	414	2	7	6089	1	2	t
18070	414	13	7	6100	2	0	t
18026	414	9	3	6096	1	2	t
17969	414	3	6	6090	0	1	t
18071	414	13	8	6100	1	0	f
18001	414	6	8	6093	1	0	f
17961	414	2	8	6089	0	1	t
17970	414	3	7	6090	1	2	f
17974	414	4	1	6091	0	2	f
18016	414	8	3	6095	1	2	t
18009	414	7	6	6094	0	2	t
17975	414	4	2	6091	0	2	f
18010	414	7	7	6094	0	2	f
18028	414	9	5	6096	1	2	t
18011	414	7	8	6094	0	2	t
18017	414	8	4	6095	0	2	f
17976	414	4	3	6091	0	1	t
17983	414	5	0	6092	0	2	f
17982	414	4	9	6091	0	1	t
18030	414	9	7	6096	1	0	f
18019	414	8	6	6095	0	2	f
17984	414	5	1	6092	0	2	f
17977	414	4	4	6091	1	2	t
18020	414	8	7	6095	0	1	t
17985	414	5	2	6092	0	1	f
18021	414	8	8	6095	1	2	f
17986	414	5	3	6092	0	2	f
17980	414	4	7	6091	0	1	f
17981	414	4	8	6091	0	2	f
17988	414	5	5	6092	1	2	t
17990	414	5	7	6092	0	1	t
17991	414	5	8	6092	1	2	t
18183	414	25	0	6112	2	1	f
18218	414	28	5	6115	0	1	t
18162	414	22	9	6109	2	0	t
18175	414	24	2	6111	2	0	t
18153	414	22	0	6109	2	1	t
18152	414	21	9	6108	2	1	t
18113	414	18	0	6105	2	1	f
18172	414	23	9	6110	2	0	f
18185	414	25	2	6112	2	1	f
18173	414	24	0	6111	2	1	f
18155	414	22	2	6109	0	1	t
18154	414	22	1	6109	2	0	t
18186	414	25	3	6112	2	1	f
18174	414	24	1	6111	2	0	f
18187	414	25	4	6112	2	0	t
18206	414	27	3	6114	0	1	f
18115	414	18	2	6105	2	0	t
18207	414	27	4	6114	0	1	t
18213	414	28	0	6115	2	1	f
18101	414	16	8	6103	1	2	t
18110	414	17	7	6104	1	0	f
18223	414	29	0	6116	2	1	t
18092	414	15	9	6102	1	0	f
18188	414	25	5	6112	0	1	f
18157	414	22	4	6109	2	0	t
18116	414	18	3	6105	0	1	f
18212	414	27	9	6114	0	1	t
18123	414	19	0	6106	2	0	t
18215	414	28	2	6115	2	0	t
18210	414	27	7	6114	2	1	f
18103	414	17	0	6104	1	2	f
18145	414	21	2	6108	0	1	t
18214	414	28	1	6115	2	1	f
18158	414	22	5	6109	0	1	t
18211	414	27	8	6114	2	0	t
18228	414	29	5	6116	2	1	f
18104	414	17	1	6104	1	2	t
18117	414	18	4	6105	0	1	f
18112	414	17	9	6104	2	0	t
18159	414	22	6	6109	2	1	t
18094	414	16	1	6103	2	0	t
18177	414	24	4	6111	2	0	t
18225	414	29	2	6116	2	1	f
18160	414	22	7	6109	2	1	f
18124	414	19	1	6106	0	1	t
18105	414	17	2	6104	2	0	f
18161	414	22	8	6109	2	1	f
18089	414	15	6	6102	2	0	t
18106	414	17	3	6104	2	0	t
18191	414	25	8	6112	2	0	t
18226	414	29	3	6116	2	1	t
18121	414	18	8	6105	2	1	f
18143	414	21	0	6108	2	1	f
18142	414	20	9	6107	2	0	t
18090	414	15	7	6102	1	0	t
18095	414	16	2	6103	1	2	t
18118	414	18	5	6105	0	2	f
18233	414	30	0	6117	2	1	f
18221	414	28	8	6115	2	0	t
18125	414	19	2	6106	2	1	f
18164	414	23	1	6110	2	1	t
18227	414	29	4	6116	2	1	f
18179	414	24	6	6111	2	1	t
18144	414	21	1	6108	2	0	t
18096	414	16	3	6103	2	0	f
18120	414	18	7	6105	0	2	t
18126	414	19	3	6106	2	0	t
18217	414	28	4	6115	2	0	t
18234	414	30	1	6117	2	1	f
18165	414	23	2	6110	2	1	f
18108	414	17	5	6104	1	0	t
18180	414	24	7	6111	2	0	t
18097	414	16	4	6103	2	0	t
18166	414	23	3	6110	2	0	t
18127	414	19	4	6106	0	1	t
18136	414	20	3	6107	2	0	t
18235	414	30	2	6117	2	0	t
18109	414	17	6	6104	1	0	t
18098	414	16	5	6103	1	0	f
18202	414	26	9	6113	2	1	t
18128	414	19	5	6106	2	0	t
18232	414	29	9	6116	0	1	t
18182	414	24	9	6111	2	1	t
18099	414	16	6	6103	1	2	t
18220	414	28	7	6115	0	1	t
18236	414	30	3	6117	0	1	t
18231	414	29	8	6116	2	0	t
18168	414	23	5	6110	2	1	f
18240	414	30	7	6117	0	1	t
18138	414	20	5	6107	2	0	t
18100	414	16	7	6103	2	0	t
18169	414	23	6	6110	2	1	t
18237	414	30	4	6117	2	0	t
18170	414	23	7	6110	2	1	f
18147	414	21	4	6108	2	1	t
18238	414	30	5	6117	0	1	t
18171	414	23	8	6110	2	1	f
18130	414	19	7	6106	2	1	t
18148	414	21	5	6108	2	1	t
18149	414	21	6	6108	2	0	t
18131	414	19	8	6106	2	0	t
18239	414	30	6	6117	2	0	t
18151	414	21	8	6108	2	1	f
18132	414	19	9	6106	0	2	t
18194	414	26	1	6113	2	1	f
18195	414	26	2	6113	2	1	f
18197	414	26	4	6113	2	1	f
18198	414	26	5	6113	2	1	f
18200	414	26	7	6113	0	1	f
18201	414	26	8	6113	0	1	t
18184	414	25	1	6112	2	0	f
17933	414	0	0	6087	0	1	t
18054	414	12	1	6099	2	0	t
18203	414	27	0	6114	2	0	f
18204	414	27	1	6114	2	1	f
18205	414	27	2	6114	2	0	t
17943	414	1	0	6088	0	2	f
18114	414	18	1	6105	2	1	f
18057	414	12	4	6099	2	0	t
18167	414	23	4	6110	0	1	t
18273	414	34	0	6121	2	1	t
18074	414	14	1	6101	2	0	t
18058	414	12	5	6099	1	2	t
18208	414	27	5	6114	2	1	t
18156	414	22	3	6109	2	1	t
18277	414	34	4	6121	2	0	f
18253	414	32	0	6119	2	1	t
18059	414	12	6	6099	2	0	f
18209	414	27	6	6114	2	1	f
18176	414	24	3	6111	0	1	t
18093	414	16	0	6103	1	2	t
17953	414	2	0	6089	0	2	f
17945	414	1	2	6088	1	2	t
17940	414	0	7	6087	1	2	f
18274	414	34	1	6121	2	1	t
18224	414	29	1	6116	2	1	t
18087	414	15	4	6102	1	2	f
18189	414	25	6	6112	0	1	t
18279	414	34	6	6121	2	1	f
18254	414	32	1	6119	2	1	t
18075	414	14	2	6101	1	0	f
18133	414	20	0	6107	2	0	t
18088	414	15	5	6102	1	2	t
18263	414	33	0	6120	2	1	t
18275	414	34	2	6121	2	1	f
17954	414	2	1	6089	0	1	t
17949	414	1	6	6088	0	2	f
18255	414	32	2	6119	2	1	f
18190	414	25	7	6112	2	1	f
17964	414	3	1	6090	1	2	t
17995	414	6	2	6093	0	2	f
17947	414	1	4	6088	1	0	f
18163	414	23	0	6110	2	1	f
18119	414	18	6	6105	0	1	f
18256	414	32	3	6119	2	0	f
18134	414	20	1	6107	0	1	f
18178	414	24	5	6111	0	2	t
18216	414	28	3	6115	0	1	t
18280	414	34	7	6121	2	0	t
18276	414	34	3	6121	2	1	f
18192	414	25	9	6112	0	1	t
18259	414	32	6	6119	2	1	t
18283	414	35	0	6122	2	1	t
18078	414	14	5	6101	2	0	t
18257	414	32	4	6119	2	1	t
18091	414	15	8	6102	1	0	f
18107	414	17	4	6104	1	0	f
18079	414	14	6	6101	1	0	t
17950	414	1	7	6088	0	1	t
18285	414	35	2	6122	2	0	t
18278	414	34	5	6121	2	1	f
18135	414	20	2	6107	0	1	t
18137	414	20	4	6107	0	1	t
18258	414	32	5	6119	2	1	f
17956	414	2	3	6089	1	2	t
18005	414	7	2	6094	0	2	f
17999	414	6	6	6093	0	1	t
18284	414	35	1	6122	2	1	t
18219	414	28	6	6115	2	0	t
18264	414	33	1	6120	2	1	f
17942	414	0	9	6087	0	2	f
17998	414	6	5	6093	0	2	t
18024	414	9	1	6096	1	2	t
18051	414	11	8	6098	2	0	f
18229	414	29	6	6116	2	0	t
18122	414	18	9	6105	2	1	t
17957	414	2	4	6089	0	1	t
18025	414	9	2	6096	2	0	t
18265	414	33	2	6120	2	0	t
18181	414	24	8	6111	0	1	t
18260	414	32	7	6119	2	1	f
18292	414	35	9	6122	2	0	t
18111	414	17	8	6104	1	2	t
18266	414	33	3	6120	0	2	f
18230	414	29	7	6116	0	1	t
18014	414	8	1	6095	1	2	t
18222	414	28	9	6115	0	1	t
18286	414	35	3	6122	0	2	t
18008	414	7	5	6094	1	2	t
18267	414	33	4	6120	0	1	t
18261	414	32	8	6119	2	1	f
17959	414	2	6	6089	0	1	t
18262	414	32	9	6119	2	1	t
18268	414	33	5	6120	2	1	t
18146	414	21	3	6108	2	1	f
18282	414	34	9	6121	2	1	f
18287	414	35	4	6122	2	1	f
18129	414	19	6	6106	0	2	t
18015	414	8	2	6095	0	1	t
18270	414	33	7	6120	0	2	t
18281	414	34	8	6121	0	1	t
18269	414	33	6	6120	2	0	t
18288	414	35	5	6122	2	0	t
18242	414	30	9	6117	0	1	t
18040	414	10	7	6097	1	0	t
18272	414	33	9	6120	0	2	t
18291	414	35	8	6122	2	1	f
18243	414	31	0	6118	2	1	t
18244	414	31	1	6118	2	1	f
18246	414	31	3	6118	2	0	t
18247	414	31	4	6118	0	1	t
18249	414	31	6	6118	2	1	f
18250	414	31	7	6118	2	0	t
18251	414	31	8	6118	0	1	t
18139	414	20	6	6107	0	1	t
18072	414	13	9	6100	1	2	t
18102	414	16	9	6103	2	0	f
17971	414	3	8	6090	1	2	t
18271	414	33	8	6120	2	0	t
18140	414	20	7	6107	2	0	t
18289	414	35	6	6122	0	1	t
18141	414	20	8	6107	0	1	t
18290	414	35	7	6122	2	1	f
17972	414	3	9	6090	0	2	f
18150	414	21	7	6108	0	1	t
18042	414	10	9	6097	1	2	t
18029	414	9	6	6096	2	0	t
18193	414	26	0	6113	2	1	t
18018	414	8	5	6095	0	1	f
18241	414	30	8	6117	2	0	t
18031	414	9	8	6096	1	2	t
17978	414	4	5	6091	0	2	f
18196	414	26	3	6113	2	1	t
18199	414	26	6	6113	2	0	t
17979	414	4	6	6091	0	2	t
18245	414	31	2	6118	2	1	f
17987	414	5	4	6092	0	1	t
18248	414	31	5	6118	2	0	f
17989	414	5	6	6092	0	1	f
18252	414	31	9	6118	2	1	t
18382	415	8	9	6131	0	3	f
18363	415	7	0	6130	0	1	f
18312	415	1	9	6124	0	3	f
18364	415	7	1	6130	0	3	f
18313	415	2	0	6125	0	3	f
18392	415	9	9	6132	0	3	f
18365	415	7	2	6130	0	2	t
18373	415	8	0	6131	0	3	f
18395	415	10	2	6133	1	2	t
18314	415	2	1	6125	0	2	t
18333	415	4	0	6127	0	3	f
18388	415	9	5	6132	0	3	t
18403	415	11	0	6134	1	0	f
18372	415	7	9	6130	0	3	f
18315	415	2	2	6125	2	3	t
18374	415	8	1	6131	0	3	t
18383	415	9	0	6132	0	3	f
18332	415	3	9	6126	1	3	t
18334	415	4	1	6127	0	3	t
18404	415	11	1	6134	1	0	f
18375	415	8	2	6131	0	3	t
18393	415	10	0	6133	1	3	t
18370	415	7	7	6130	2	1	f
18335	415	4	2	6127	0	3	f
18376	415	8	3	6131	0	3	t
18302	415	0	9	6123	1	2	f
18293	415	0	0	6123	0	1	f
18402	415	10	9	6133	1	2	t
18316	415	2	3	6125	0	1	t
18323	415	3	0	6126	0	2	t
18322	415	2	9	6125	2	3	f
18336	415	4	3	6127	0	3	f
18343	415	5	0	6128	0	2	f
18318	415	2	5	6125	0	2	t
18385	415	9	2	6132	0	3	t
18317	415	2	4	6125	1	3	t
18378	415	8	5	6131	0	1	f
18303	415	1	0	6124	0	3	f
18324	415	3	1	6126	2	3	t
18294	415	0	1	6123	0	2	t
18394	415	10	1	6133	3	0	t
18379	415	8	6	6131	0	3	t
18391	415	9	8	6132	0	3	f
18387	415	9	4	6132	0	3	f
18344	415	5	1	6128	0	3	t
18380	415	8	7	6131	0	3	f
18406	415	11	3	6134	2	0	t
18326	415	3	3	6126	1	3	t
18340	415	4	7	6127	0	3	t
18319	415	2	6	6125	2	3	t
18390	415	9	7	6132	0	3	f
18407	415	11	4	6134	1	0	t
18304	415	1	1	6124	0	1	t
18408	415	11	5	6134	1	0	f
18345	415	5	2	6128	0	1	t
18320	415	2	7	6125	0	1	f
18297	415	0	4	6123	2	3	t
18327	415	3	4	6126	0	1	t
18328	415	3	5	6126	1	3	t
18397	415	10	4	6133	1	0	t
18321	415	2	8	6125	0	2	t
18346	415	5	3	6128	1	3	t
18329	415	3	6	6126	0	3	f
18398	415	10	5	6133	1	0	t
18347	415	5	4	6128	0	2	t
18306	415	1	3	6124	2	3	t
18296	415	0	3	6123	0	2	t
18348	415	5	5	6128	2	3	f
18331	415	3	8	6126	0	1	t
18400	415	10	7	6133	3	0	t
18401	415	10	8	6133	1	0	f
18349	415	5	6	6128	2	3	t
18362	415	6	9	6129	2	3	t
18350	415	5	7	6128	0	2	t
18299	415	0	6	6123	1	2	t
18351	415	5	8	6128	2	3	t
18300	415	0	7	6123	2	3	t
18352	415	5	9	6128	0	1	t
18310	415	1	7	6124	0	2	t
18311	415	1	8	6124	2	3	t
18301	415	0	8	6123	0	1	t
18355	415	6	2	6129	1	3	t
18357	415	6	4	6129	1	3	t
18358	415	6	5	6129	0	1	t
18360	415	6	7	6129	1	0	f
18361	415	6	8	6129	1	2	t
18433	415	14	0	6137	1	0	f
18525	415	23	2	6146	2	1	t
18563	415	27	0	6150	2	3	t
18546	415	25	3	6148	2	3	t
18523	415	23	0	6146	2	3	t
18553	415	26	0	6149	2	0	t
18524	415	23	1	6146	3	2	t
18413	415	12	0	6135	1	2	t
18449	415	15	6	6138	2	3	f
18424	415	13	1	6136	1	0	f
18414	415	12	1	6135	2	0	t
18436	415	14	3	6137	1	3	f
18427	415	13	4	6136	3	1	f
18425	415	13	2	6136	1	3	t
18503	415	21	0	6144	2	1	t
18485	415	19	2	6142	1	3	t
18415	415	12	2	6135	1	0	f
18552	415	25	9	6148	2	0	f
18438	415	14	5	6137	2	0	f
18416	415	12	3	6135	1	2	t
18439	415	14	6	6137	2	0	t
18533	415	24	0	6147	2	1	t
18527	415	23	4	6146	2	0	f
18440	415	14	7	6137	1	2	t
18417	415	12	4	6135	2	0	t
18528	415	23	5	6146	2	3	f
18505	415	21	2	6144	2	1	t
18529	415	23	6	6146	2	0	f
18555	415	26	2	6149	2	3	t
18443	415	15	0	6138	1	0	f
18522	415	22	9	6145	2	1	f
18493	415	20	0	6143	2	1	f
18442	415	14	9	6137	1	2	t
18422	415	12	9	6135	1	2	t
18530	415	23	7	6146	2	3	t
18419	415	12	6	6135	3	0	t
18494	415	20	1	6143	2	1	f
18429	415	13	6	6136	3	2	t
18513	415	22	0	6145	2	1	t
18556	415	26	3	6149	3	1	t
18444	415	15	1	6138	1	2	t
18545	415	25	2	6148	0	1	t
18430	415	13	7	6136	2	1	t
18483	415	19	0	6142	1	2	t
18463	415	17	0	6140	1	0	f
18420	415	12	7	6135	1	2	f
18495	415	20	2	6143	2	0	t
18421	415	12	8	6135	1	0	f
18431	415	13	8	6136	1	3	t
18508	415	21	5	6144	2	0	t
18514	415	22	1	6145	2	0	t
18432	415	13	9	6136	3	2	f
18509	415	21	6	6144	0	1	t
18534	415	24	1	6147	2	0	t
18547	415	25	4	6148	3	1	t
18479	415	18	6	6141	1	2	f
18496	415	20	3	6143	0	3	t
18542	415	24	9	6147	2	0	t
18515	415	22	2	6145	0	1	f
18511	415	21	8	6144	3	1	t
18558	415	26	5	6149	0	1	t
18480	415	18	7	6141	1	2	t
18510	415	21	7	6144	2	3	t
18447	415	15	4	6138	3	0	t
18535	415	24	2	6147	0	3	f
18410	415	11	7	6134	1	2	t
18559	415	26	6	6149	2	1	t
18516	415	22	3	6145	0	1	f
18487	415	19	4	6142	3	1	t
18498	415	20	5	6143	2	1	t
18448	415	15	5	6138	1	2	t
18411	415	11	8	6134	2	0	t
18536	415	24	3	6147	0	2	f
18562	415	26	9	6149	0	1	t
18551	415	25	8	6148	3	1	t
18497	415	20	4	6143	3	1	t
18561	415	26	8	6149	2	0	t
18453	415	16	0	6139	1	2	t
18412	415	11	9	6134	1	0	f
18537	415	24	4	6147	0	1	t
18462	415	16	9	6139	3	2	t
18465	415	17	2	6140	2	3	t
18473	415	18	0	6141	1	0	t
18490	415	19	7	6142	2	3	t
18518	415	22	5	6145	0	3	f
18489	415	19	6	6142	1	2	t
18454	415	16	1	6139	2	0	t
18451	415	15	8	6138	1	0	t
18539	415	24	6	6147	0	1	t
18452	415	15	9	6138	1	3	t
18540	415	24	7	6147	2	0	t
18502	415	20	9	6143	3	1	t
18455	415	16	2	6139	1	0	t
18474	415	18	1	6141	1	0	f
18541	415	24	8	6147	0	1	t
18467	415	17	4	6140	1	0	f
18501	415	20	8	6143	2	3	t
18456	415	16	3	6139	1	3	f
18469	415	17	6	6140	2	0	t
18475	415	18	2	6141	1	2	f
18476	415	18	3	6141	1	3	t
18470	415	17	7	6140	1	0	f
18471	415	17	8	6140	1	2	t
18458	415	16	5	6139	2	0	f
18478	415	18	5	6141	3	0	t
18520	415	22	7	6145	0	2	f
18459	415	16	6	6139	2	0	f
18460	415	16	7	6139	2	3	t
18521	415	22	8	6145	0	2	t
18461	415	16	8	6139	3	0	f
18423	415	13	0	6136	1	2	f
18434	415	14	1	6137	1	2	t
18633	415	34	0	6157	3	2	f
18573	415	28	0	6151	2	1	t
18663	415	37	0	6160	3	2	f
18435	415	14	2	6137	2	0	t
18543	415	25	0	6148	2	1	f
18683	415	39	0	6162	3	0	t
18366	415	7	3	6130	2	3	f
18437	415	14	4	6137	1	2	t
18574	415	28	1	6151	2	1	f
18622	415	32	9	6155	3	0	t
18593	415	30	0	6153	3	2	f
18368	415	7	5	6130	2	0	f
18664	415	37	1	6160	3	0	t
18367	415	7	4	6130	2	1	f
18650	415	35	7	6158	0	2	f
18665	415	37	2	6160	0	1	f
18554	415	26	1	6149	0	1	t
18613	415	32	0	6155	3	2	f
18682	415	38	9	6161	3	2	f
18634	415	34	1	6157	3	0	t
18684	415	39	1	6162	0	1	t
18575	415	28	2	6151	2	1	f
18592	415	29	9	6152	0	1	t
18583	415	29	0	6152	2	1	f
18369	415	7	6	6130	2	3	f
18526	415	23	3	6146	2	1	f
18426	415	13	3	6136	3	0	f
18662	415	36	9	6159	0	2	t
18666	415	37	3	6160	0	1	t
18594	415	30	1	6153	3	0	t
18504	415	21	1	6144	2	1	f
18672	415	37	9	6160	3	0	t
18635	415	34	2	6157	0	2	t
18614	415	32	1	6155	3	2	f
18688	415	39	5	6162	1	0	t
18576	415	28	3	6151	2	0	t
18636	415	34	3	6157	3	2	f
18685	415	39	2	6162	1	3	t
18673	415	38	0	6161	3	2	t
18572	415	27	9	6150	3	1	t
18577	415	28	4	6151	0	1	f
18667	415	37	4	6160	1	2	t
18584	415	29	1	6152	2	1	f
18642	415	34	9	6157	3	2	f
18638	415	34	5	6157	1	3	f
18643	415	35	0	6158	3	2	t
18655	415	36	2	6159	3	1	t
18653	415	36	0	6159	3	2	t
18674	415	38	1	6161	3	0	t
18623	415	33	0	6156	3	2	f
18582	415	28	9	6151	2	1	t
18686	415	39	3	6162	3	2	f
18616	415	32	3	6155	1	3	t
18604	415	31	1	6154	3	1	t
18586	415	29	3	6152	0	1	t
18578	415	28	5	6151	0	1	t
18654	415	36	1	6159	3	0	f
18596	415	30	3	6153	0	1	f
18640	415	34	7	6157	1	2	t
18644	415	35	1	6158	3	0	f
18617	415	32	4	6155	3	1	f
18587	415	29	4	6152	2	3	t
18589	415	29	6	6152	2	1	f
18605	415	31	2	6154	1	2	t
18618	415	32	5	6155	3	0	t
18597	415	30	4	6153	0	3	f
18579	415	28	6	6151	2	1	f
18588	415	29	5	6152	3	1	t
18619	415	32	6	6155	0	1	t
18645	415	35	2	6158	3	1	f
18624	415	33	1	6156	3	0	t
18598	415	30	5	6153	0	2	t
18580	415	28	7	6151	2	1	t
18620	415	32	7	6155	1	2	t
18606	415	31	3	6154	3	2	f
18646	415	35	3	6158	3	2	f
18581	415	28	8	6151	2	1	t
18652	415	35	9	6158	3	2	f
18676	415	38	3	6161	3	1	t
18602	415	30	9	6153	3	0	t
18628	415	33	5	6156	3	1	t
18625	415	33	2	6156	0	2	t
18657	415	36	4	6159	3	0	t
18632	415	33	9	6156	3	0	t
18677	415	38	4	6161	1	2	t
18599	415	30	6	6153	3	2	f
18658	415	36	5	6159	0	1	f
18608	415	31	5	6154	3	0	t
18678	415	38	5	6161	3	0	t
18626	415	33	3	6156	3	2	f
18659	415	36	6	6159	0	1	t
18648	415	35	5	6158	0	1	f
18609	415	31	6	6154	0	1	t
18691	415	39	8	6162	0	1	t
18601	415	30	8	6153	0	2	t
18649	415	35	6	6158	0	3	f
18610	415	31	7	6154	1	2	f
18627	415	33	4	6156	3	2	f
18661	415	36	8	6159	0	3	f
18611	415	31	8	6154	1	2	t
18565	415	27	2	6150	3	0	t
18612	415	31	9	6154	3	2	f
18680	415	38	7	6161	0	1	t
18566	415	27	3	6150	0	1	t
18681	415	38	8	6161	1	2	t
18567	415	27	4	6150	2	3	t
18568	415	27	5	6150	3	0	t
18569	415	27	6	6150	0	1	t
18571	415	27	8	6150	0	3	t
18384	415	9	1	6132	0	3	t
18371	415	7	8	6130	2	0	t
18377	415	8	4	6131	0	3	f
18441	415	14	8	6137	2	0	t
18405	415	11	2	6134	1	2	t
18615	415	32	2	6155	3	1	t
18637	415	34	4	6157	3	1	t
18418	415	12	5	6135	1	3	t
18603	415	31	0	6154	3	2	f
18337	415	4	4	6127	0	3	f
18544	415	25	1	6148	2	0	t
18428	415	13	5	6136	3	0	f
18585	415	29	2	6152	2	0	t
18506	415	21	3	6144	2	1	f
18338	415	4	5	6127	0	3	t
18668	415	37	5	6160	3	0	t
18639	415	34	6	6157	1	2	f
18386	415	9	3	6132	0	3	t
18531	415	23	8	6146	3	0	f
18595	415	30	2	6153	0	2	f
18325	415	3	2	6126	0	1	t
18507	415	21	4	6144	2	1	f
18339	415	4	6	6127	0	3	f
18532	415	23	9	6146	3	2	t
18669	415	37	6	6160	0	2	t
18445	415	15	2	6138	2	0	t
18687	415	39	4	6162	3	1	t
18389	415	9	6	6132	0	3	f
18484	415	19	1	6142	2	1	t
18381	415	8	8	6131	0	3	t
18670	415	37	7	6160	3	1	t
18641	415	34	8	6157	3	2	t
18341	415	4	8	6127	0	3	t
18557	415	26	4	6149	2	0	t
18671	415	37	8	6160	1	2	t
18396	415	10	3	6133	2	0	t
18446	415	15	3	6138	1	3	t
18342	415	4	9	6127	0	3	f
18548	415	25	5	6148	2	1	f
18409	415	11	6	6134	1	3	f
18675	415	38	2	6161	0	2	t
18549	415	25	6	6148	2	0	f
18305	415	1	2	6124	1	2	t
18590	415	29	7	6152	2	0	t
18656	415	36	3	6159	1	3	t
18486	415	19	3	6142	3	2	f
18295	415	0	2	6123	2	3	t
18689	415	39	6	6162	0	3	t
18550	415	25	7	6148	2	3	t
18621	415	32	8	6155	3	2	f
18591	415	29	8	6152	0	3	f
18464	415	17	1	6140	1	2	t
18560	415	26	7	6149	2	1	f
18512	415	21	9	6144	2	1	t
18607	415	31	4	6154	3	2	t
18647	415	35	4	6158	3	0	t
18330	415	3	7	6126	0	2	f
18517	415	22	4	6145	0	2	f
18690	415	39	7	6162	3	0	t
18399	415	10	6	6133	1	3	t
18488	415	19	5	6142	1	0	f
18450	415	15	7	6138	2	0	t
18538	415	24	5	6147	2	0	t
18600	415	30	7	6153	3	0	t
18564	415	27	1	6150	3	0	f
18307	415	1	4	6124	0	3	f
18660	415	36	7	6159	1	0	t
18499	415	20	6	6143	2	0	t
18679	415	38	6	6161	0	2	f
18491	415	19	8	6142	3	1	f
18466	415	17	3	6140	3	0	t
18298	415	0	5	6123	0	1	t
18500	415	20	7	6143	0	1	t
18692	415	39	9	6162	1	0	f
18492	415	19	9	6142	3	2	t
18308	415	1	5	6124	0	1	f
18519	415	22	6	6145	0	2	f
18651	415	35	8	6158	0	3	t
18629	415	33	6	6156	1	2	t
18309	415	1	6	6124	0	2	f
18468	415	17	5	6140	1	2	t
18353	415	6	0	6129	0	3	f
18630	415	33	7	6156	3	1	t
18457	415	16	4	6139	1	2	t
18354	415	6	1	6129	0	1	t
18631	415	33	8	6156	1	2	t
18477	415	18	4	6141	3	1	f
18472	415	17	9	6140	2	0	t
18481	415	18	8	6141	2	3	t
18356	415	6	3	6129	0	1	t
18570	415	27	7	6150	2	0	t
18482	415	18	9	6141	3	0	t
18359	415	6	6	6129	1	3	f
18720	416	2	7	6165	0	1	t
18712	416	1	9	6164	0	2	f
18715	416	2	2	6165	0	1	t
18723	416	3	0	6166	0	2	f
18702	416	0	9	6163	0	1	t
18717	416	2	4	6165	0	2	f
18718	416	2	5	6165	0	1	t
18719	416	2	6	6165	1	2	t
18704	416	1	1	6164	0	1	t
18724	416	3	1	6166	0	2	t
18705	416	1	2	6164	1	2	f
18706	416	1	3	6164	1	2	f
18707	416	1	4	6164	1	0	f
18732	416	3	9	6166	0	2	f
18700	416	0	7	6163	0	2	f
18708	416	1	5	6164	1	2	f
18709	416	1	6	6164	1	2	f
18710	416	1	7	6164	1	2	t
18726	416	3	3	6166	0	2	t
18727	416	3	4	6166	0	2	t
18729	416	3	6	6166	0	2	t
18730	416	3	7	6166	0	2	t
18833	416	14	0	6177	1	0	f
18803	416	11	0	6174	1	0	f
18835	416	14	2	6177	2	0	t
18763	416	7	0	6170	0	2	t
18861	416	16	8	6179	1	2	t
18842	416	14	9	6177	1	0	f
18744	416	5	1	6168	0	2	t
18773	416	8	0	6171	0	2	t
18792	416	9	9	6172	0	1	t
18764	416	7	1	6170	0	2	t
18882	416	18	9	6181	1	2	t
18734	416	4	1	6167	0	1	t
18752	416	5	9	6168	0	2	f
18837	416	14	4	6177	2	0	t
18765	416	7	2	6170	0	2	f
18774	416	8	1	6171	0	1	t
18766	416	7	3	6170	0	1	t
18853	416	16	0	6179	1	0	f
18735	416	4	2	6167	1	2	t
18883	416	19	0	6182	1	2	t
18802	416	10	9	6173	2	0	t
18793	416	10	0	6173	1	0	f
18838	416	14	5	6177	1	2	t
18775	416	8	2	6171	1	2	f
18778	416	8	5	6171	1	2	t
18767	416	7	4	6170	1	2	t
18884	416	19	1	6182	2	0	t
18854	416	16	1	6179	1	0	t
18772	416	7	9	6170	0	1	t
18843	416	15	0	6178	1	0	f
18750	416	5	7	6168	1	2	t
18813	416	12	0	6175	1	0	f
18812	416	11	9	6174	1	0	f
18776	416	8	3	6171	1	0	t
18805	416	11	2	6174	1	0	t
18737	416	4	4	6167	1	0	f
18769	416	7	6	6170	0	1	f
18777	416	8	4	6171	0	1	t
18864	416	17	1	6180	1	2	t
18738	416	4	5	6167	1	2	t
18770	416	7	7	6170	0	2	f
18855	416	16	2	6179	1	0	t
18844	416	15	1	6178	1	2	f
18739	416	4	6	6167	0	2	f
18865	416	17	2	6180	2	0	t
18771	416	7	8	6170	0	1	f
18886	416	19	3	6182	1	2	t
18856	416	16	3	6179	1	0	t
18740	416	4	7	6167	0	2	f
18815	416	12	2	6175	2	0	f
18748	416	5	5	6168	0	2	t
18845	416	15	2	6178	1	0	t
18742	416	4	9	6167	1	2	t
18822	416	12	9	6175	1	2	f
18866	416	17	3	6180	1	2	t
18741	416	4	8	6167	0	1	t
18867	416	17	4	6180	2	0	t
18816	416	12	3	6175	2	1	t
18749	416	5	6	6168	0	1	t
18841	416	14	8	6177	1	0	f
18783	416	9	0	6172	0	1	t
18781	416	8	8	6171	0	2	f
18859	416	16	6	6179	1	2	t
18873	416	18	0	6181	1	0	t
18762	416	6	9	6169	1	0	t
18817	416	12	4	6175	1	0	t
18846	416	15	3	6178	1	0	f
18754	416	6	1	6169	1	2	t
18872	416	17	9	6180	1	2	f
18847	416	15	4	6178	1	2	f
18860	416	16	7	6179	2	0	t
18784	416	9	1	6172	1	2	t
18869	416	17	6	6180	2	0	t
18823	416	13	0	6176	1	0	f
18880	416	18	7	6181	1	0	f
18818	416	12	5	6175	1	2	t
18807	416	11	4	6174	1	0	t
18848	416	15	5	6178	1	0	f
18819	416	12	6	6175	2	1	t
18870	416	17	7	6180	1	2	t
18755	416	6	2	6169	0	1	t
18852	416	15	9	6178	2	1	f
18820	416	12	7	6175	1	0	t
18849	416	15	6	6178	1	2	t
18799	416	10	6	6173	1	2	t
18875	416	18	2	6181	1	0	f
18785	416	9	2	6172	0	1	t
18821	416	12	8	6175	1	0	f
18876	416	18	3	6181	1	0	f
18809	416	11	6	6174	1	2	t
18824	416	13	1	6176	1	0	f
18877	416	18	4	6181	1	2	t
18825	416	13	2	6176	1	2	t
18786	416	9	3	6172	1	2	t
18810	416	11	7	6174	2	0	t
18757	416	6	4	6169	0	1	t
18787	416	9	4	6172	0	1	t
18879	416	18	6	6181	2	0	t
18811	416	11	8	6174	1	0	f
18826	416	13	3	6176	2	0	t
18788	416	9	5	6172	1	2	t
18759	416	6	6	6169	1	2	t
18830	416	13	7	6176	2	0	t
18789	416	9	6	6172	0	2	f
18760	416	6	7	6169	0	1	t
18761	416	6	8	6169	1	2	f
18828	416	13	5	6176	1	2	t
18829	416	13	6	6176	2	1	f
18791	416	9	8	6172	1	2	t
18832	416	13	9	6176	1	0	t
18834	416	14	1	6177	1	2	t
18716	416	2	3	6165	1	2	t
18953	416	26	0	6189	2	0	t
18713	416	2	0	6165	0	2	f
18943	416	25	0	6188	2	0	f
18954	416	26	1	6189	0	1	t
18733	416	4	0	6167	0	1	f
18836	416	14	3	6177	1	2	t
18714	416	2	1	6165	0	2	t
18945	416	25	2	6188	0	2	f
18923	416	23	0	6186	2	1	f
18745	416	5	2	6168	0	2	f
18944	416	25	1	6188	2	0	t
18914	416	22	1	6185	2	0	f
18963	416	27	0	6190	2	1	t
18743	416	5	0	6168	0	2	t
18958	416	26	5	6189	2	1	t
18955	416	26	2	6189	2	1	t
18804	416	11	1	6174	1	0	f
18956	416	26	3	6189	2	0	t
18924	416	23	1	6186	2	0	t
18964	416	27	1	6190	2	1	f
18697	416	0	4	6163	1	2	t
18973	416	28	0	6191	2	1	f
18966	416	27	3	6190	0	1	f
18957	416	26	4	6189	0	1	t
18768	416	7	5	6170	0	2	t
18693	416	0	0	6163	0	2	f
18965	416	27	2	6190	2	0	t
18974	416	28	1	6191	2	1	f
18925	416	23	2	6186	0	1	t
18703	416	1	0	6164	0	2	t
18747	416	5	4	6168	1	2	t
18913	416	22	0	6185	2	1	f
18962	416	26	9	6189	2	0	f
18983	416	29	0	6192	2	1	f
18863	416	17	0	6180	1	2	f
18959	416	26	6	6189	2	0	t
18746	416	5	3	6168	0	1	t
18736	416	4	3	6167	0	1	t
18885	416	19	2	6182	1	0	t
18926	416	23	3	6186	2	0	f
18814	416	12	1	6175	1	2	t
18960	416	26	7	6189	0	2	f
18694	416	0	1	6163	0	2	t
18839	416	14	6	6177	2	0	f
18971	416	27	8	6190	2	1	f
18946	416	25	3	6188	0	1	f
18984	416	29	1	6192	2	0	t
18975	416	28	2	6191	2	1	t
18892	416	19	9	6182	2	0	f
18927	416	23	4	6186	2	1	t
18721	416	2	8	6165	1	2	t
18967	416	27	4	6190	0	1	t
18961	416	26	8	6189	0	1	t
18695	416	0	2	6163	0	2	t
18928	416	23	5	6186	2	1	f
18779	416	8	6	6171	0	2	f
18976	416	28	3	6191	2	1	t
18985	416	29	2	6192	0	2	t
18696	416	0	3	6163	0	1	t
18902	416	20	9	6183	0	1	t
18929	416	23	6	6186	2	0	f
18988	416	29	5	6192	2	0	t
18968	416	27	5	6190	2	1	t
18951	416	25	8	6188	2	1	t
18977	416	28	4	6191	2	1	t
18932	416	23	9	6186	2	0	t
18947	416	25	4	6188	0	2	t
18986	416	29	3	6192	2	0	t
18794	416	10	1	6173	1	2	t
18806	416	11	3	6174	1	0	t
18933	416	24	0	6187	2	0	t
18931	416	23	8	6186	0	2	t
18969	416	27	6	6190	2	1	f
18970	416	27	7	6190	2	0	f
18980	416	28	7	6191	2	1	f
18948	416	25	5	6188	2	1	f
18903	416	21	0	6184	2	1	t
18912	416	21	9	6184	2	1	f
18987	416	29	4	6192	0	1	t
18981	416	28	8	6191	2	1	f
18889	416	19	6	6182	2	0	f
18917	416	22	4	6185	0	2	t
18890	416	19	7	6182	2	0	t
18922	416	22	9	6185	2	1	t
18904	416	21	1	6184	2	0	f
18918	416	22	5	6185	2	0	t
18949	416	25	6	6188	2	0	f
18891	416	19	8	6182	1	2	t
18905	416	21	2	6184	2	1	f
18950	416	25	7	6188	2	0	f
18919	416	22	6	6185	0	2	t
18992	416	29	9	6192	2	0	t
18906	416	21	3	6184	2	1	t
18921	416	22	8	6185	0	2	t
18935	416	24	2	6187	2	1	t
18907	416	21	4	6184	2	1	t
18909	416	21	6	6184	2	1	t
18893	416	20	0	6183	2	1	f
18942	416	24	9	6187	2	1	f
18911	416	21	8	6184	2	1	f
18936	416	24	3	6187	2	1	f
18894	416	20	1	6183	2	0	t
18938	416	24	5	6187	2	1	f
18939	416	24	6	6187	2	1	f
18941	416	24	8	6187	2	1	f
18895	416	20	2	6183	0	1	t
18897	416	20	4	6183	0	1	t
18898	416	20	5	6183	2	0	f
18900	416	20	7	6183	0	1	t
18901	416	20	8	6183	2	0	t
18915	416	22	2	6185	2	1	t
18840	416	14	7	6177	2	1	t
18930	416	23	7	6186	2	0	t
18857	416	16	4	6179	1	0	t
18978	416	28	5	6191	2	1	f
18753	416	6	0	6169	0	1	t
18780	416	8	7	6171	0	2	t
18887	416	19	4	6182	2	1	t
18722	416	2	9	6165	0	1	t
18858	416	16	5	6179	1	0	f
18979	416	28	6	6191	2	1	f
18916	416	22	3	6185	2	0	t
18795	416	10	2	6173	2	1	t
18698	416	0	5	6163	0	2	f
18888	416	19	5	6182	1	2	t
18782	416	8	9	6171	0	2	f
18796	416	10	3	6173	1	2	t
18725	416	3	2	6166	0	2	t
18868	416	17	5	6180	1	2	t
18699	416	0	6	6163	0	2	f
18797	416	10	4	6173	2	0	t
18982	416	28	9	6191	2	1	f
18972	416	27	9	6190	2	1	f
18874	416	18	1	6181	1	0	f
18751	416	5	8	6168	0	2	t
18798	416	10	5	6173	1	0	f
18701	416	0	8	6163	0	2	f
18871	416	17	8	6180	2	0	t
18989	416	29	6	6192	0	2	t
18808	416	11	5	6174	1	2	f
18862	416	16	9	6179	2	0	f
18800	416	10	7	6173	2	0	f
18990	416	29	7	6192	2	0	t
18801	416	10	8	6173	2	1	f
18991	416	29	8	6192	0	2	t
18711	416	1	8	6164	0	2	t
18934	416	24	1	6187	0	1	t
18756	416	6	3	6169	1	2	t
18920	416	22	7	6185	2	0	t
18878	416	18	5	6181	2	1	f
18850	416	15	7	6178	2	1	t
18758	416	6	5	6169	1	2	f
18908	416	21	5	6184	2	1	t
18952	416	25	9	6188	2	0	t
18910	416	21	7	6184	2	1	t
18881	416	18	8	6181	1	0	t
18827	416	13	4	6176	1	0	t
18851	416	15	8	6178	1	2	t
18937	416	24	4	6187	2	1	f
18790	416	9	7	6172	0	1	t
18940	416	24	7	6187	2	1	f
18831	416	13	8	6176	1	0	f
18728	416	3	5	6166	0	2	t
18896	416	20	3	6183	2	0	t
18731	416	3	8	6166	0	2	f
18899	416	20	6	6183	2	0	t
19010	417	1	7	6194	0	1	t
19013	417	2	0	6195	0	3	t
19022	417	2	9	6195	2	3	t
19014	417	2	1	6195	0	3	t
19015	417	2	2	6195	0	1	t
19023	417	3	0	6196	0	3	t
19016	417	2	3	6195	1	0	f
19024	417	3	1	6196	0	3	t
19017	417	2	4	6195	1	3	t
19018	417	2	5	6195	0	3	f
19025	417	3	2	6196	0	3	f
19019	417	2	6	6195	0	3	t
19026	417	3	3	6196	0	3	f
19043	417	5	0	6198	0	3	t
19052	417	5	9	6198	2	0	t
19027	417	3	4	6196	0	3	t
19020	417	2	7	6195	0	2	t
19028	417	3	5	6196	0	3	t
19021	417	2	8	6195	2	3	f
19029	417	3	6	6196	0	3	f
19044	417	5	1	6198	0	3	f
19030	417	3	7	6196	0	3	t
19045	417	5	2	6198	0	1	t
19031	417	3	8	6196	0	3	t
19053	417	6	0	6199	0	3	f
19032	417	3	9	6196	0	3	f
19046	417	5	3	6198	1	2	t
19047	417	5	4	6198	2	3	t
19054	417	6	1	6199	0	1	t
19048	417	5	5	6198	0	3	f
19003	417	1	0	6194	0	3	f
19042	417	4	9	6197	1	3	t
19049	417	5	6	6198	0	2	t
19055	417	6	2	6199	1	3	t
19004	417	1	1	6194	0	3	f
19033	417	4	0	6197	0	1	t
19057	417	6	4	6199	2	3	f
19050	417	5	7	6198	2	3	f
19056	417	6	3	6199	0	2	t
19005	417	1	2	6194	0	1	t
19051	417	5	8	6198	2	1	f
19006	417	1	3	6194	1	3	t
19034	417	4	1	6197	1	2	t
19035	417	4	2	6197	2	3	f
18993	417	0	0	6193	0	3	f
18995	417	0	2	6193	1	3	t
19009	417	1	6	6194	0	3	f
19036	417	4	3	6197	2	3	t
18994	417	0	1	6193	0	1	t
19002	417	0	9	6193	0	2	t
19037	417	4	4	6197	0	1	t
19038	417	4	5	6197	1	3	t
18996	417	0	3	6193	0	2	t
19040	417	4	7	6197	1	3	t
19041	417	4	8	6197	0	1	t
18998	417	0	5	6193	1	2	f
18999	417	0	6	6193	1	3	t
19001	417	0	8	6193	1	3	t
19193	417	20	0	6213	2	1	t
19202	417	20	9	6213	0	1	t
19062	417	6	9	6199	1	3	f
19059	417	6	6	6199	0	3	t
19113	417	12	0	6205	1	0	f
19065	417	7	2	6200	0	3	f
19183	417	19	0	6212	1	0	f
19186	417	19	3	6212	1	3	f
19094	417	10	1	6203	1	2	t
19114	417	12	1	6205	1	2	t
19184	417	19	1	6212	1	2	t
19143	417	15	0	6208	1	0	f
19096	417	10	3	6203	1	3	t
19123	417	13	0	6206	1	0	f
19084	417	9	1	6202	0	3	f
19095	417	10	2	6203	2	0	t
19116	417	12	3	6205	1	0	f
19198	417	20	5	6213	2	3	t
19124	417	13	1	6206	1	0	f
19185	417	19	2	6212	2	0	t
19117	417	12	4	6205	1	3	t
19079	417	8	6	6201	0	1	t
19144	417	15	1	6208	1	3	f
19122	417	12	9	6205	3	2	f
19097	417	10	4	6203	3	0	t
19153	417	16	0	6209	1	2	t
19098	417	10	5	6203	1	2	t
19118	417	12	5	6205	3	2	f
19119	417	12	6	6205	3	1	f
19074	417	8	1	6201	0	3	t
19126	417	13	3	6206	1	3	t
19200	417	20	7	6213	2	1	f
19145	417	15	2	6208	1	0	f
19120	417	12	7	6205	3	0	t
19099	417	10	6	6203	2	0	t
19070	417	7	7	6200	1	3	t
19063	417	7	0	6200	0	3	t
19131	417	13	8	6206	1	0	t
19154	417	16	1	6209	2	3	t
19127	417	13	4	6206	3	0	t
19201	417	20	8	6213	2	0	t
19146	417	15	3	6208	1	2	t
19103	417	11	0	6204	1	0	f
19082	417	8	9	6201	0	3	t
19077	417	8	4	6201	2	3	t
19128	417	13	5	6206	1	2	f
19101	417	10	8	6203	3	0	f
19088	417	9	5	6202	1	2	f
19203	417	21	0	6214	2	1	f
19142	417	14	9	6207	1	0	t
19083	417	9	0	6202	0	3	t
19211	417	21	8	6214	2	3	t
19104	417	11	1	6204	1	3	t
19191	417	19	8	6212	1	2	f
19078	417	8	5	6201	0	3	f
19064	417	7	1	6200	0	1	f
19192	417	19	9	6212	1	3	t
19204	417	21	1	6214	2	1	t
19130	417	13	7	6206	3	0	t
19182	417	18	9	6211	1	3	t
19148	417	15	5	6208	1	2	f
19156	417	16	3	6209	1	0	t
19080	417	8	7	6201	1	3	t
19105	417	11	2	6204	3	2	t
19149	417	15	6	6208	1	0	f
19058	417	6	5	6199	2	3	t
19081	417	8	8	6201	0	3	f
19157	417	16	4	6209	1	2	t
19150	417	15	7	6208	1	3	t
19106	417	11	3	6204	2	0	f
19174	417	18	1	6211	1	2	t
19158	417	16	5	6209	2	3	t
19163	417	17	0	6210	1	0	t
19152	417	15	9	6208	3	2	f
19159	417	16	6	6209	3	0	t
19092	417	9	9	6202	1	3	t
19090	417	9	7	6202	1	3	t
19162	417	16	9	6209	1	3	t
19151	417	15	8	6208	3	1	f
19107	417	11	4	6204	2	0	t
19061	417	6	8	6199	0	1	t
19175	417	18	2	6211	2	3	f
19068	417	7	5	6200	0	3	f
19108	417	11	5	6204	1	2	f
19207	417	21	4	6214	0	1	t
19069	417	7	6	6200	0	1	t
19109	417	11	6	6204	1	3	t
19208	417	21	5	6214	2	1	t
19165	417	17	2	6210	1	0	f
19176	417	18	3	6211	2	1	f
19209	417	21	6	6214	2	0	t
19110	417	11	7	6204	3	0	t
19177	417	18	4	6211	2	0	t
19210	417	21	7	6214	0	2	t
19166	417	17	3	6210	1	2	f
19112	417	11	9	6204	2	0	t
19178	417	18	5	6211	1	3	f
19172	417	17	9	6210	1	0	f
19167	417	17	4	6210	1	0	f
19111	417	11	8	6204	1	2	t
19179	417	18	6	6211	1	2	t
19168	417	17	5	6210	1	3	t
19180	417	18	7	6211	2	1	t
19169	417	17	6	6210	3	0	f
19181	417	18	8	6211	1	0	f
19170	417	17	7	6210	3	0	t
19171	417	17	8	6210	1	0	t
19138	417	14	5	6207	1	0	t
19140	417	14	7	6207	1	0	t
19141	417	14	8	6207	1	0	f
19213	417	22	0	6215	2	1	t
19222	417	22	9	6215	2	0	t
19306	417	31	3	6224	2	1	t
19293	417	30	0	6223	2	1	f
19285	417	29	2	6222	2	0	f
19297	417	30	4	6223	3	1	t
19217	417	22	4	6215	2	1	f
19215	417	22	2	6215	3	1	t
19314	417	32	1	6225	2	1	t
19216	417	22	3	6215	2	1	t
19253	417	26	0	6219	2	1	f
19336	417	34	3	6227	2	1	f
19334	417	34	1	6227	2	0	f
19273	417	28	0	6221	2	1	t
19312	417	31	9	6224	2	1	t
19326	417	33	3	6226	3	0	f
19274	417	28	1	6221	2	1	f
19335	417	34	2	6227	2	3	f
19302	417	30	9	6223	2	1	f
19254	417	26	1	6219	2	3	t
19219	417	22	6	6215	2	1	f
19295	417	30	2	6223	2	1	f
19283	417	29	0	6222	2	1	f
19342	417	34	9	6227	2	1	t
19220	417	22	7	6215	2	3	t
19255	417	26	2	6219	3	1	t
19275	417	28	2	6221	2	3	t
19343	417	35	0	6228	2	1	f
19318	417	32	5	6225	2	1	f
19221	417	22	8	6215	3	1	t
19328	417	33	5	6226	3	0	t
19316	417	32	3	6225	0	1	t
19303	417	31	0	6224	2	1	t
19256	417	26	3	6219	2	0	f
19338	417	34	5	6227	2	0	t
19276	417	28	3	6221	3	2	t
19304	417	31	1	6224	2	1	t
19344	417	35	1	6228	2	1	t
19257	417	26	4	6219	2	1	t
19317	417	32	4	6225	2	1	t
19212	417	21	9	6214	3	1	t
19223	417	23	0	6216	2	0	t
19322	417	32	9	6225	0	3	f
19352	417	35	9	6228	0	1	f
19258	417	26	5	6219	2	0	f
19345	417	35	2	6228	2	1	f
19299	417	30	6	6223	0	1	t
19259	417	26	6	6219	2	3	t
19339	417	34	6	6227	0	1	t
19277	417	28	4	6221	2	1	t
19272	417	27	9	6220	2	1	t
19260	417	26	7	6219	3	2	f
19224	417	23	1	6216	0	1	t
19300	417	30	7	6223	2	3	t
19262	417	26	9	6219	2	1	f
19308	417	31	5	6224	2	1	t
19332	417	33	9	6226	2	0	t
19340	417	34	7	6227	2	3	t
19311	417	31	8	6224	2	1	t
19309	417	31	6	6224	2	1	f
19330	417	33	7	6226	2	0	t
19287	417	29	4	6222	3	2	t
19279	417	28	6	6221	0	1	t
19310	417	31	7	6224	2	1	f
19225	417	23	2	6216	2	1	t
19363	417	37	0	6230	2	1	t
19282	417	28	9	6221	2	1	f
19348	417	35	5	6228	2	1	f
19288	417	29	5	6222	2	0	t
19280	417	28	7	6221	2	0	f
19349	417	35	6	6228	2	1	t
19226	417	23	3	6216	2	3	t
19281	417	28	8	6221	2	1	t
19365	417	37	2	6230	2	0	t
19263	417	27	0	6220	2	1	t
19359	417	36	6	6229	0	1	f
19364	417	37	1	6230	2	1	f
19227	417	23	4	6216	3	1	t
19290	417	29	7	6222	2	1	f
19291	417	29	8	6222	2	3	t
19228	417	23	5	6216	2	1	t
19292	417	29	9	6222	3	1	t
19265	417	27	2	6220	2	3	t
19229	417	23	6	6216	2	0	t
19230	417	23	7	6216	0	1	t
19231	417	23	8	6216	2	3	t
19266	417	27	3	6220	3	1	t
19267	417	27	4	6220	2	1	t
19353	417	36	0	6229	2	1	t
19357	417	36	4	6229	2	1	t
19268	417	27	5	6220	2	1	f
19246	417	25	3	6218	2	0	f
19354	417	36	1	6229	2	3	t
19247	417	25	4	6218	2	1	f
19355	417	36	2	6229	3	1	f
19271	417	27	8	6220	0	1	t
19356	417	36	3	6229	3	1	t
19249	417	25	6	6218	2	1	t
19250	417	25	7	6218	2	1	f
19251	417	25	8	6218	2	0	f
19252	417	25	9	6218	2	3	t
19242	417	24	9	6217	2	1	t
19361	417	36	8	6229	2	3	t
19362	417	36	9	6229	3	1	f
19234	417	24	1	6217	3	1	t
19235	417	24	2	6217	2	1	f
19237	417	24	4	6217	0	1	t
19238	417	24	5	6217	2	3	t
19240	417	24	7	6217	3	1	t
19241	417	24	8	6217	2	0	f
19373	417	38	0	6231	2	1	f
19519	417	52	6	6245	1	0	f
19432	417	43	9	6236	1	2	t
19453	417	46	0	6239	3	2	f
19423	417	43	0	6236	3	2	f
19512	417	51	9	6244	3	1	t
19375	417	38	2	6231	0	3	t
19440	417	44	7	6237	3	1	t
19424	417	43	1	6236	3	2	f
19376	417	38	3	6231	3	1	f
19414	417	42	1	6235	3	2	t
19434	417	44	1	6237	3	0	t
19377	417	38	4	6231	3	2	t
19427	417	43	4	6236	0	3	f
19415	417	42	2	6235	3	2	t
19416	417	42	3	6235	3	0	t
19378	417	38	5	6231	2	3	t
19382	417	38	9	6231	2	1	t
19403	417	41	0	6234	3	0	f
19391	417	39	8	6232	0	2	t
19383	417	39	0	6232	2	1	f
19492	417	49	9	6242	3	2	t
19429	417	43	6	6236	3	2	t
19379	417	38	6	6231	3	0	f
19435	417	44	2	6237	0	2	t
19430	417	43	7	6236	3	1	t
19418	417	42	5	6235	3	2	t
19380	417	38	7	6231	3	2	t
19384	417	39	1	6232	2	1	f
19490	417	49	7	6242	3	2	t
19485	417	49	2	6242	0	2	f
19431	417	43	8	6236	1	2	f
19405	417	41	2	6234	3	2	f
19381	417	38	8	6231	2	0	f
19385	417	39	2	6232	2	3	t
19486	417	49	3	6242	0	3	t
19436	417	44	3	6237	3	2	f
19437	417	44	4	6237	3	1	t
19514	417	52	1	6245	3	0	t
19406	417	41	3	6234	3	1	t
19493	417	50	0	6243	3	2	f
19422	417	42	9	6235	3	2	f
19438	417	44	5	6237	1	0	t
19488	417	49	5	6242	1	2	t
19482	417	48	9	6241	0	2	t
19387	417	39	4	6232	2	0	t
19439	417	44	6	6237	0	2	t
19388	417	39	5	6232	0	2	t
19489	417	49	6	6242	3	0	f
19407	417	41	4	6234	1	2	t
19516	417	52	3	6245	0	1	t
19389	417	39	6	6232	2	3	t
19443	417	45	0	6238	3	2	f
19368	417	37	5	6230	3	1	t
19390	417	39	7	6232	3	0	t
19412	417	41	9	6234	0	1	f
19506	417	51	3	6244	1	3	t
19464	417	47	1	6240	3	2	f
19408	417	41	5	6234	3	1	t
19444	417	45	1	6238	3	1	t
19517	417	52	4	6245	1	3	f
19409	417	41	6	6234	1	2	t
19442	417	44	9	6237	1	2	t
19518	417	52	5	6245	1	2	f
19393	417	40	0	6233	3	2	f
19496	417	50	3	6243	3	0	t
19498	417	50	5	6243	3	1	f
19445	417	45	2	6238	1	2	t
19396	417	40	3	6233	3	2	f
19503	417	51	0	6244	3	2	f
19452	417	45	9	6238	1	2	f
19411	417	41	8	6234	0	3	f
19394	417	40	1	6233	3	2	f
19446	417	45	3	6238	3	0	f
19366	417	37	3	6230	0	1	t
19466	417	47	3	6240	0	2	t
19504	417	51	1	6244	3	2	f
19501	417	50	8	6243	3	0	t
19447	417	45	4	6238	3	1	t
19367	417	37	4	6230	2	3	t
19500	417	50	7	6243	3	2	f
19473	417	48	0	6241	3	2	f
19472	417	47	9	6240	3	0	t
19505	417	51	2	6244	3	1	t
19467	417	47	4	6240	3	1	t
19448	417	45	5	6238	1	2	t
19468	417	47	5	6240	1	2	f
19449	417	45	6	6238	3	0	t
19474	417	48	1	6241	3	2	f
19450	417	45	7	6238	0	2	t
19372	417	37	9	6230	2	3	t
19476	417	48	3	6241	3	2	t
19370	417	37	7	6230	2	0	t
19458	417	46	5	6239	3	0	t
19469	417	47	6	6240	1	0	f
19371	417	37	8	6230	0	1	t
19461	417	46	8	6239	3	1	t
19470	417	47	7	6240	1	2	f
19459	417	46	6	6239	0	2	t
19479	417	48	6	6241	3	1	f
19471	417	47	8	6240	1	3	t
19480	417	48	7	6241	3	2	f
19460	417	46	7	6239	3	0	f
19509	417	51	6	6244	1	3	t
19481	417	48	8	6241	3	0	t
19510	417	51	7	6244	3	2	f
19402	417	40	9	6233	3	1	t
19398	417	40	5	6233	1	2	t
19400	417	40	7	6233	0	2	t
19401	417	40	8	6233	3	2	t
19218	417	22	5	6215	2	0	f
19553	417	56	0	6249	3	2	f
19428	417	43	5	6236	0	2	t
19554	417	56	1	6249	3	2	t
19583	417	59	0	6252	3	2	f
19315	417	32	2	6225	2	0	t
19555	417	56	2	6249	3	1	f
19483	417	49	0	6242	3	2	f
19556	417	56	3	6249	3	0	f
19374	417	38	1	6231	2	0	t
19323	417	33	0	6226	2	1	f
19584	417	59	1	6252	3	2	f
19194	417	20	1	6213	2	1	t
19413	417	42	0	6235	3	2	t
19592	417	59	9	6252	0	2	t
19557	417	56	4	6249	3	2	t
19093	417	10	0	6203	1	0	f
19313	417	32	0	6225	2	1	t
19588	417	59	5	6252	3	2	f
19558	417	56	5	6249	3	2	t
19433	417	44	0	6237	3	2	f
19214	417	22	1	6215	2	3	t
19195	417	20	2	6213	2	1	t
19298	417	30	5	6223	2	0	t
19559	417	56	6	6249	3	2	f
19333	417	34	0	6227	2	1	t
19575	417	58	2	6251	3	1	t
19585	417	59	2	6252	3	1	f
19196	417	20	3	6213	2	1	f
19073	417	8	0	6201	0	3	t
19560	417	56	7	6249	3	2	t
19425	417	43	2	6236	3	2	t
19417	417	42	4	6235	0	2	t
19573	417	58	0	6251	3	2	f
19561	417	56	8	6249	3	2	f
19125	417	13	2	6206	1	2	f
19586	417	59	3	6252	3	1	t
19426	417	43	3	6236	3	0	t
19576	417	58	3	6251	1	3	t
19543	417	55	0	6248	3	2	t
19562	417	56	9	6249	3	2	f
19294	417	30	1	6223	2	0	f
19197	417	20	4	6213	2	1	f
19115	417	12	2	6205	2	0	t
19419	417	42	6	6235	3	2	f
19587	417	59	4	6252	1	2	t
19325	417	33	2	6226	2	3	t
19574	417	58	1	6251	3	0	f
19199	417	20	6	6213	3	1	t
19484	417	49	1	6242	3	0	t
19589	417	59	6	6252	3	2	f
19286	417	29	3	6222	2	3	t
19544	417	55	1	6248	3	0	t
19296	417	30	3	6223	2	3	t
19190	417	19	7	6212	2	0	t
19523	417	53	0	6246	3	2	t
19324	417	33	1	6226	2	0	f
19577	417	58	4	6251	3	2	t
19590	417	59	7	6252	3	2	f
19404	417	41	1	6234	3	1	f
19513	417	52	0	6245	3	2	f
19284	417	29	1	6222	2	1	t
19337	417	34	4	6227	2	1	f
19187	417	19	4	6212	1	0	f
19075	417	8	2	6201	0	3	f
19532	417	53	9	6246	3	2	f
19591	417	59	8	6252	3	0	t
19420	417	42	7	6235	3	2	t
19188	417	19	5	6212	1	2	t
19121	417	12	8	6205	1	3	t
19421	417	42	8	6235	3	2	t
19076	417	8	3	6201	0	2	t
19524	417	53	1	6246	3	2	f
19578	417	58	5	6251	3	2	t
19305	417	31	2	6224	2	1	t
19327	417	33	4	6226	3	1	f
19100	417	10	7	6203	1	3	t
19487	417	49	4	6242	3	1	t
19189	417	19	6	6212	2	3	f
19386	417	39	3	6232	3	1	t
19155	417	16	2	6209	3	0	t
19329	417	33	6	6226	0	1	t
19579	417	58	6	6251	3	2	f
19319	417	32	6	6225	2	0	t
19533	417	54	0	6247	3	2	t
19546	417	55	3	6248	3	1	t
19580	417	58	7	6251	3	2	f
19552	417	55	9	6248	0	2	t
19545	417	55	2	6248	0	2	t
19549	417	55	6	6248	0	2	t
19581	417	58	8	6251	3	2	t
19582	417	58	9	6251	3	2	f
19526	417	53	3	6246	1	2	t
19535	417	54	2	6247	3	2	f
19536	417	54	3	6247	3	2	f
19537	417	54	4	6247	3	1	t
19538	417	54	5	6247	1	2	t
19563	417	57	0	6250	3	0	t
19548	417	55	5	6248	3	0	t
19539	417	54	6	6247	3	1	f
19529	417	53	6	6246	0	2	t
19541	417	54	8	6247	0	2	t
19520	417	52	7	6245	1	0	f
19521	417	52	8	6245	1	3	t
19530	417	53	7	6246	3	1	t
19551	417	55	8	6248	3	0	t
19531	417	53	8	6246	1	2	t
19564	417	57	1	6250	0	3	f
19566	417	57	3	6250	0	2	t
19567	417	57	4	6250	3	1	t
19569	417	57	6	6250	1	2	t
19570	417	57	7	6250	3	1	t
19571	417	57	8	6250	1	2	t
19307	417	31	4	6224	2	1	f
19463	417	47	0	6240	3	2	f
19147	417	15	4	6208	2	0	t
19525	417	53	2	6246	3	1	t
19129	417	13	6	6206	1	3	t
19346	417	35	3	6228	2	1	t
19515	417	52	2	6245	0	3	f
19173	417	18	0	6211	1	0	t
19261	417	26	8	6219	3	1	t
19278	417	28	5	6221	2	0	t
19102	417	10	9	6203	3	2	f
19534	417	54	1	6247	3	2	t
19301	417	30	8	6223	3	1	t
19347	417	35	4	6228	2	1	f
19331	417	33	8	6226	0	1	t
19494	417	50	1	6243	3	1	t
19341	417	34	8	6227	3	1	t
19007	417	1	4	6194	0	2	t
19320	417	32	7	6225	0	1	f
19491	417	49	8	6242	3	0	f
19132	417	13	9	6206	1	0	t
19441	417	44	8	6237	1	2	f
19066	417	7	3	6200	0	2	t
19008	417	1	5	6194	2	0	t
19495	417	50	2	6243	1	2	t
19350	417	35	7	6228	2	1	f
19321	417	32	8	6225	0	2	f
19547	417	55	4	6248	1	3	t
19392	417	39	9	6232	2	3	t
19527	417	53	4	6246	3	2	f
19085	417	9	2	6202	0	3	t
19351	417	35	8	6228	2	0	t
19205	417	21	2	6214	2	1	f
19289	417	29	6	6222	0	1	t
19060	417	6	7	6199	0	3	f
19086	417	9	3	6202	0	1	t
19067	417	7	4	6200	2	3	t
19410	417	41	7	6234	3	0	t
19206	417	21	3	6214	2	0	t
19011	417	1	8	6194	1	3	t
19528	417	53	5	6246	3	0	t
19465	417	47	2	6240	3	0	t
19454	417	46	1	6239	3	2	t
19264	417	27	1	6220	2	1	f
19012	417	1	9	6194	0	1	t
19160	417	16	7	6209	1	2	f
19497	417	50	4	6243	0	2	t
19164	417	17	1	6210	1	0	t
19540	417	54	7	6247	3	0	t
19243	417	25	0	6218	2	1	t
19455	417	46	2	6239	3	2	f
19087	417	9	4	6202	1	3	f
19161	417	16	8	6209	1	2	f
19456	417	46	3	6239	3	2	f
19244	417	25	1	6218	2	1	f
19039	417	4	6	6197	0	1	t
19542	417	54	9	6247	3	0	t
19499	417	50	6	6243	3	2	t
19550	417	55	7	6248	3	2	f
19089	417	9	6	6202	1	0	f
19457	417	46	4	6239	3	2	t
19395	417	40	2	6233	3	1	f
19522	417	52	9	6245	3	1	f
19232	417	23	9	6216	3	1	t
19071	417	7	8	6200	0	3	t
19502	417	50	9	6243	0	2	f
19091	417	9	8	6202	0	1	t
19133	417	14	0	6207	1	0	f
19072	417	7	9	6200	0	3	f
19245	417	25	2	6218	2	1	f
19134	417	14	1	6207	1	2	t
19369	417	37	6	6230	2	1	f
19475	417	48	2	6241	3	2	f
18997	417	0	4	6193	2	1	t
19451	417	45	8	6238	3	1	t
19135	417	14	2	6207	2	0	f
19269	417	27	6	6220	2	3	f
19477	417	48	4	6241	3	0	t
19507	417	51	4	6244	3	2	t
19136	417	14	3	6207	2	0	f
19248	417	25	5	6218	2	1	t
19270	417	27	7	6220	2	0	t
19000	417	0	7	6193	0	1	t
19137	417	14	4	6207	2	0	t
19478	417	48	5	6241	0	2	t
19508	417	51	5	6244	3	1	t
19139	417	14	6	6207	1	0	f
19462	417	46	9	6239	1	0	f
19511	417	51	8	6244	3	2	f
19358	417	36	5	6229	2	0	t
19397	417	40	4	6233	3	1	t
19360	417	36	7	6229	0	2	t
19233	417	24	0	6217	2	3	t
19399	417	40	6	6233	3	0	t
19236	417	24	3	6217	2	0	t
19565	417	57	2	6250	0	1	f
19239	417	24	6	6217	3	0	f
19568	417	57	5	6250	1	0	f
19572	417	57	9	6250	3	0	t
\.


--
-- Data for Name: game_type; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.game_type (id, room_id, player_id, user_id, production_good) FROM stdin;
2822	85	46	4842	2
2823	85	47	4843	2
2824	85	48	4844	2
2825	85	49	4845	2
2776	85	0	4756	0
2777	85	1	4758	0
2778	85	2	4762	0
2779	85	3	4766	0
2780	85	4	4769	0
2781	85	5	4773	0
2782	85	6	4776	0
2783	85	7	4778	0
2784	85	8	4782	0
2785	85	9	4787	0
2786	85	10	4790	0
2787	85	11	4792	0
2788	85	12	4797	0
2789	85	13	4798	0
2790	85	14	4799	0
2791	85	15	4800	1
2792	85	16	4804	1
2793	85	17	4805	1
2794	85	18	4806	1
2795	85	19	4807	1
2796	85	20	4808	1
2797	85	21	4811	1
2798	85	22	4812	1
2799	85	23	4814	1
2800	85	24	4816	1
2801	85	25	4818	1
2802	85	26	4819	1
2803	85	27	4822	1
2804	85	28	4824	1
2805	85	29	4825	1
2806	85	30	4826	2
2807	85	31	4827	2
2808	85	32	4828	2
2809	85	33	4829	2
2810	85	34	4830	2
2811	85	35	4831	2
2812	85	36	4832	2
2813	85	37	4833	2
2814	85	38	4834	2
2815	85	39	4835	2
2816	85	40	4836	2
2817	85	41	4837	2
2818	85	42	4838	2
2819	85	43	4839	2
2820	85	44	4840	2
2821	85	45	4841	2
\.


--
-- Data for Name: game_user; Type: TABLE DATA; Schema: public; Owner: dasein
--

COPY public.game_user (id, room_id, device_id, player_id, pseudo, age, gender, production_good, consumption_good, score, tutorial_done, tutorial_score, state, training_done, training_score, tablet_id) FROM stdin;
6129	415	\N	6	Authaire	40	female	0	3	18	\N	\N	end	t	7	38
6153	415	\N	30	Francaire	24	male	3	2	29	\N	\N	end	t	5	91
6133	415	\N	10	Caribert	62	female	1	0	25	\N	\N	end	t	9	2
6139	415	\N	16	Drogon	20	male	1	0	24	\N	\N	end	t	6	50
6112	414	\N	25	Frajou	18	female	2	1	18	\N	\N	end	t	4	51
6102	414	\N	15	Conan	25	male	1	0	49	\N	\N	end	t	5	53
6089	414	\N	2	Achard	21	female	0	2	29	\N	\N	end	t	8	7
6110	414	\N	23	Fortunat	28	female	2	1	16	\N	\N	end	t	4	58
6096	414	\N	9	Bérard	22	female	1	0	44	\N	\N	end	t	8	0
6143	415	\N	20	Flour	24	male	2	1	16	\N	\N	end	t	8	98
6107	414	\N	20	Flour	20	male	2	1	19	\N	\N	end	t	9	6
6111	414	\N	24	Foulque	23	male	2	1	13	\N	\N	end	t	8	95
6117	414	\N	30	Francaire	20	male	2	1	12	\N	\N	end	t	8	37
6100	414	\N	13	Clodomir	23	female	1	0	44	\N	\N	end	t	8	99
6106	414	\N	19	Flouard	23	female	2	1	19	\N	\N	end	t	9	96
6108	414	\N	21	Floxel	21	male	2	1	18	\N	\N	end	t	7	3
6118	414	\N	31	Fulbert	25	male	2	1	16	\N	\N	end	t	6	91
6101	414	\N	14	Clotaire	32	female	1	0	24	\N	\N	end	t	7	56
6103	414	\N	16	Drogon	20	female	1	0	17	\N	\N	end	t	7	36
6159	415	\N	36	Guiscard	59	female	3	2	14	\N	\N	end	t	7	8
6122	414	\N	35	Guibin	29	male	2	1	18	\N	\N	end	t	7	90
6147	415	\N	24	Foulque	30	female	2	1	28	\N	\N	end	t	8	34
6099	414	\N	12	Childebert	39	male	1	0	23	\N	\N	end	t	8	98
6113	414	\N	26	Flocel	52	female	2	1	18	\N	\N	end	t	5	39
6104	414	\N	17	Durand	21	female	1	0	30	\N	\N	end	t	6	32
6114	414	\N	27	Frambault	27	male	2	1	16	\N	\N	end	t	5	92
6137	415	\N	14	Clotaire	25	female	1	0	20	\N	\N	end	t	7	39
6127	415	\N	4	Agrève	22	male	0	3	30	\N	\N	end	t	4	31
6141	415	\N	18	Flodoard	22	male	1	0	32	\N	\N	end	t	6	96
6177	416	\N	14	Clotaire	24	female	1	0	29	\N	\N	end	t	6	32
6155	415	\N	32	Gaillon	22	male	3	2	23	\N	\N	end	t	6	59
6123	415	\N	0	Arthur	28	female	0	3	15	\N	\N	end	t	8	10
6125	415	\N	2	Achard	22	male	0	3	20	\N	\N	end	t	7	6
6167	416	\N	4	Agrève	21	male	0	2	27	\N	\N	end	t	6	6
6151	415	\N	28	Frambourg	24	male	2	1	33	\N	\N	end	t	6	94
6226	417	\N	33	Gaubert	19	male	2	1	16	\N	\N	end	t	6	44
6135	415	\N	12	Childebert	18	male	1	0	17	\N	\N	end	t	7	57
6131	415	\N	8	Barral	19	male	0	3	26	\N	\N	end	t	5	32
6192	416	\N	29	Frameric	65	male	2	1	35	\N	\N	end	t	9	31
6157	415	\N	34	Guéthenoc	23	male	3	2	16	\N	\N	end	t	5	30
6145	415	\N	22	Folquet	22	female	2	1	30	\N	\N	end	t	3	52
6189	416	\N	26	Flocel	20	male	2	1	37	\N	\N	end	t	8	53
6161	415	\N	38	Haynhard	19	female	3	2	26	\N	\N	end	t	8	100
6169	416	\N	6	Authaire	40	female	0	2	22	\N	\N	end	t	8	51
6171	416	\N	8	Barral	27	male	0	2	30	\N	\N	end	t	6	57
6191	416	\N	28	Frambourg	51	male	2	1	33	\N	\N	end	t	3	39
6194	417	\N	1	Abrand	58	male	0	3	40	\N	\N	end	t	7	3
6175	416	\N	12	Childebert	28	female	1	0	30	\N	\N	end	t	6	37
6187	416	\N	24	Foulque	24	male	2	1	22	\N	\N	end	t	3	59
6220	417	\N	27	Frambault	25	male	2	1	13	\N	\N	end	t	7	45
6163	416	\N	0	Arthur	21	male	0	2	36	\N	\N	end	t	5	0
6173	416	\N	10	Caribert	22	female	1	0	27	\N	\N	end	t	6	55
6149	415	\N	26	Flocel	25	female	2	1	23	\N	\N	end	t	9	95
6208	417	\N	15	Conan	24	female	1	0	21	\N	\N	end	t	3	43
6232	417	\N	39	Héribert	56	female	2	1	9	\N	\N	end	t	8	35
6183	416	\N	20	Flour	25	female	2	1	21	\N	\N	end	t	8	35
6198	417	\N	5	Anselin	21	male	0	3	34	\N	\N	end	t	6	56
6179	416	\N	16	Drogon	31	female	1	0	26	\N	\N	end	t	7	7
6165	416	\N	2	Achard	24	female	0	2	24	\N	\N	end	t	8	30
6212	417	\N	19	Flouard	21	female	1	0	33	\N	\N	end	t	5	42
6181	416	\N	18	Flodoard	20	female	1	0	27	\N	\N	end	t	5	60
6185	416	\N	22	Folquet	43	female	2	1	21	\N	\N	end	t	8	50
6204	417	\N	11	Centule	24	male	1	0	33	\N	\N	end	t	7	96
6218	417	\N	25	Frajou	62	female	2	1	17	\N	\N	end	t	4	36
6206	417	\N	13	Clodomir	22	male	1	0	37	\N	\N	end	t	6	41
6210	417	\N	17	Durand	27	female	1	0	41	\N	\N	end	t	5	58
6219	417	\N	26	Flocel	26	male	2	1	11	\N	\N	end	t	5	89
6184	416	\N	21	Floxel	21	female	2	1	30	\N	\N	end	t	6	52
6132	415	\N	9	Bérard	27	male	0	3	29	\N	\N	end	t	4	99
6091	414	\N	4	Agrève	26	male	0	2	36	\N	\N	end	t	5	31
6095	414	\N	8	Barral	39	female	0	2	21	\N	\N	end	t	6	100
6098	414	\N	11	Centule	22	male	1	0	34	\N	\N	end	t	6	34
6115	414	\N	28	Frambourg	21	female	2	1	19	\N	\N	end	t	8	94
6088	414	\N	1	Abrand	21	male	0	2	38	\N	\N	end	t	6	55
6120	414	\N	33	Gaubert	55	female	2	1	10	\N	\N	end	t	8	30
6121	414	\N	34	Guéthenoc	27	male	2	1	18	\N	\N	end	t	4	60
6119	414	\N	32	Gaillon	68	male	2	1	23	\N	\N	end	t	5	33
6093	414	\N	6	Authaire	26	female	0	2	44	\N	\N	end	t	5	57
6090	414	\N	3	Agelmar	24	male	0	2	39	\N	\N	end	t	8	9
6087	414	\N	0	Arthur	22	male	0	2	46	\N	\N	end	t	8	52
6128	415	\N	5	Anselin	25	male	0	3	28	\N	\N	end	t	8	9
6097	414	\N	10	Caribert	23	male	1	0	48	\N	\N	end	t	8	59
6109	414	\N	22	Folquet	23	male	2	1	18	\N	\N	end	t	8	50
6148	415	\N	25	Frajou	45	female	2	1	20	\N	\N	end	t	6	3
6094	414	\N	7	Avold	21	female	0	2	39	\N	\N	end	t	7	38
6150	415	\N	27	Frambault	25	female	2	1	15	\N	\N	end	t	9	7
6116	414	\N	29	Frameric	20	male	2	1	23	\N	\N	end	t	7	10
6092	414	\N	5	Anselin	31	female	0	2	23	\N	\N	end	t	4	2
6105	414	\N	18	Flodoard	22	male	2	1	19	\N	\N	end	t	3	5
6124	415	\N	1	Abrand	28	male	0	3	23	\N	\N	end	t	5	37
6140	415	\N	17	Durand	28	male	1	0	19	\N	\N	end	t	7	5
6134	415	\N	11	Centule	20	female	1	0	26	\N	\N	end	t	5	60
6160	415	\N	37	Hatton	54	female	3	2	16	\N	\N	end	t	8	51
6146	415	\N	23	Fortunat	23	female	2	1	22	\N	\N	end	t	5	93
6162	415	\N	39	Héribert	65	female	3	2	26	\N	\N	end	t	8	55
6152	415	\N	29	Frameric	25	male	2	1	17	\N	\N	end	t	6	33
6158	415	\N	35	Guibin	24	male	3	2	22	\N	\N	end	t	3	58
6136	415	\N	13	Clodomir	19	male	1	0	25	\N	\N	end	t	4	56
6186	416	\N	23	Fortunat	63	female	2	1	23	\N	\N	end	t	6	5
6154	415	\N	31	Fulbert	66	female	3	2	35	\N	\N	end	t	6	4
6126	415	\N	3	Agelmar	20	female	0	3	19	\N	\N	end	t	8	92
6138	415	\N	15	Conan	22	female	1	0	26	\N	\N	end	t	8	35
6217	417	\N	24	Foulque	23	female	2	1	13	\N	\N	end	t	7	63
6156	415	\N	33	Gaubert	23	female	3	2	23	\N	\N	end	t	7	36
6144	415	\N	21	Floxel	20	male	2	1	26	\N	\N	end	t	7	53
6130	415	\N	7	Avold	22	female	0	3	23	\N	\N	end	t	2	90
6142	415	\N	19	Flouard	22	female	1	0	18	\N	\N	end	t	7	0
6164	416	\N	1	Abrand	25	male	0	2	32	\N	\N	end	t	4	3
6168	416	\N	5	Anselin	23	female	0	2	30	\N	\N	end	t	8	10
6166	416	\N	3	Agelmar	55	male	0	2	30	\N	\N	end	t	7	8
6172	416	\N	9	Bérard	26	male	0	2	23	\N	\N	end	t	9	4
6199	417	\N	6	Authaire	22	male	0	3	33	\N	\N	end	t	6	64
6170	416	\N	7	Avold	36	male	0	2	27	\N	\N	end	t	6	33
6180	416	\N	17	Durand	21	male	1	0	24	\N	\N	end	t	8	56
6233	417	\N	40	Herlemond	21	female	3	2	14	\N	\N	end	t	6	51
6229	417	\N	36	Guiscard	31	male	2	1	17	\N	\N	end	t	7	19
6176	416	\N	13	Clodomir	20	female	1	0	33	\N	\N	end	t	6	9
6205	417	\N	12	Childebert	22	male	1	0	35	\N	\N	end	t	5	37
6174	416	\N	11	Centule	34	male	1	0	28	\N	\N	end	t	5	2
6190	416	\N	27	Frambault	42	female	2	1	33	\N	\N	end	t	4	36
6178	416	\N	15	Conan	24	male	1	0	33	\N	\N	end	t	4	38
6188	416	\N	25	Frajou	64	female	2	1	27	\N	\N	end	t	4	58
6227	417	\N	34	Guéthenoc	22	female	2	1	15	\N	\N	end	t	6	99
6182	416	\N	19	Flouard	22	female	1	0	24	\N	\N	end	t	8	34
6203	417	\N	10	Caribert	25	male	1	0	28	\N	\N	end	t	7	95
6215	417	\N	22	Folquet	20	male	2	1	18	\N	\N	end	t	7	30
6237	417	\N	44	Isembert	27	male	3	2	19	\N	\N	end	t	7	86
6197	417	\N	4	Agrève	25	male	0	3	23	\N	\N	end	t	9	6
6209	417	\N	16	Drogon	22	female	1	0	16	\N	\N	end	t	8	61
6235	417	\N	42	Honfroi	22	male	3	2	22	\N	\N	end	t	8	93
6239	417	\N	46	Jacut	24	male	3	2	17	\N	\N	end	t	5	55
6207	417	\N	14	Clotaire	19	female	1	0	39	\N	\N	end	t	5	22
6223	417	\N	30	Francaire	20	female	2	1	17	\N	\N	end	t	6	88
6250	417	\N	57	Sigebert	27	female	3	2	17	\N	\N	end	t	7	62
6228	417	\N	35	Guibin	20	male	2	1	14	\N	\N	end	t	4	9
6225	417	\N	32	Gaillon	25	male	2	1	17	\N	\N	end	t	6	50
6242	417	\N	49	Lancelin	43	male	3	2	17	\N	\N	end	t	6	53
6216	417	\N	23	Fortunat	19	female	2	1	22	\N	\N	end	t	10	10
6238	417	\N	45	Jacquemin	65	female	3	2	16	\N	\N	end	t	7	21
6195	417	\N	2	Achard	27	male	0	3	34	\N	\N	end	t	7	83
6231	417	\N	38	Haynhard	23	female	2	1	7	\N	\N	end	t	6	23
6234	417	\N	41	Hoel	24	female	3	2	17	\N	\N	end	t	5	91
6213	417	\N	20	Flour	22	female	2	1	14	\N	\N	end	t	7	65
6224	417	\N	31	Fulbert	49	female	2	1	14	\N	\N	end	t	7	57
6230	417	\N	37	Hatton	22	female	2	1	19	\N	\N	end	t	8	4
6200	417	\N	7	Avold	27	male	0	3	34	\N	\N	end	t	6	100
6245	417	\N	52	Milon	18	female	3	2	13	\N	\N	end	t	3	98
6201	417	\N	8	Barral	31	female	0	3	30	\N	\N	end	t	7	7
6244	417	\N	51	Mesmin	18	female	3	2	11	\N	\N	end	t	6	92
6246	417	\N	53	Odo	65	female	3	2	6	\N	\N	end	t	7	38
6243	417	\N	50	Lothaire	27	male	3	2	16	\N	\N	end	t	6	0
6236	417	\N	43	Hugon	23	female	3	2	16	\N	\N	end	t	6	90
6196	417	\N	3	Agelmar	28	male	0	3	32	\N	\N	end	t	6	39
6222	417	\N	29	Frameric	24	male	2	1	19	\N	\N	end	t	7	34
6202	417	\N	9	Bérard	24	male	0	3	25	\N	\N	end	t	6	52
6252	417	\N	59	Vantelme	27	male	3	2	16	\N	\N	end	t	4	59
6211	417	\N	18	Flodoard	66	female	1	0	20	\N	\N	end	t	6	5
6240	417	\N	47	Lagier	20	female	3	2	17	\N	\N	end	t	5	31
6214	417	\N	21	Floxel	21	male	2	1	15	\N	\N	end	t	8	84
6247	417	\N	54	Perceval	26	female	3	2	16	\N	\N	end	t	7	24
6193	417	\N	0	Arthur	41	male	0	3	24	\N	\N	end	t	8	33
6251	417	\N	58	Taillefer	49	female	3	2	18	\N	\N	end	t	5	94
6241	417	\N	48	Lancelot	25	male	3	2	14	\N	\N	end	t	5	2
6221	417	\N	28	Frambourg	20	male	2	1	17	\N	\N	end	t	7	32
6248	417	\N	55	Sicard	39	female	3	2	10	\N	\N	end	t	9	8
6249	417	\N	56	Sifard	29	male	3	2	16	\N	\N	end	t	4	60
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 60, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: dashboard_connectedtablet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.dashboard_connectedtablet_id_seq', 118, true);


--
-- Name: dashboard_intparameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.dashboard_intparameter_id_seq', 2, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 60, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 20, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 48, true);


--
-- Name: game_boolparameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.game_boolparameter_id_seq', 9, true);


--
-- Name: game_choice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.game_choice_id_seq', 109960, true);


--
-- Name: game_floatparameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.game_floatparameter_id_seq', 1, false);


--
-- Name: game_intparameter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.game_intparameter_id_seq', 14, true);


--
-- Name: game_probaexchangetraining_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.game_probaexchangetraining_id_seq', 14, true);


--
-- Name: game_room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.game_room_id_seq', 417, true);


--
-- Name: game_tutorialchoice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.game_tutorialchoice_id_seq', 19592, true);


--
-- Name: game_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.game_type_id_seq', 2825, true);


--
-- Name: game_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dasein
--

SELECT pg_catalog.setval('public.game_user_id_seq', 6252, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: dashboard_connectedtablet dashboard_connectedtablet_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.dashboard_connectedtablet
    ADD CONSTRAINT dashboard_connectedtablet_pkey PRIMARY KEY (id);


--
-- Name: dashboard_intparameter dashboard_intparameter_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.dashboard_intparameter
    ADD CONSTRAINT dashboard_intparameter_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: game_boolparameter game_boolparameter_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_boolparameter
    ADD CONSTRAINT game_boolparameter_pkey PRIMARY KEY (id);


--
-- Name: game_choice game_choice_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_choice
    ADD CONSTRAINT game_choice_pkey PRIMARY KEY (id);


--
-- Name: game_choice game_choice_user_id_t_1900b078_uniq; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_choice
    ADD CONSTRAINT game_choice_user_id_t_1900b078_uniq UNIQUE (user_id, t);


--
-- Name: game_floatparameter game_floatparameter_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_floatparameter
    ADD CONSTRAINT game_floatparameter_pkey PRIMARY KEY (id);


--
-- Name: game_intparameter game_intparameter_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_intparameter
    ADD CONSTRAINT game_intparameter_pkey PRIMARY KEY (id);


--
-- Name: game_probaexchangetraining game_probaexchangetraining_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_probaexchangetraining
    ADD CONSTRAINT game_probaexchangetraining_pkey PRIMARY KEY (id);


--
-- Name: game_room game_room_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_room
    ADD CONSTRAINT game_room_pkey PRIMARY KEY (id);


--
-- Name: game_tutorialchoice game_tutorialchoice_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_tutorialchoice
    ADD CONSTRAINT game_tutorialchoice_pkey PRIMARY KEY (id);


--
-- Name: game_type game_type_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_type
    ADD CONSTRAINT game_type_pkey PRIMARY KEY (id);


--
-- Name: game_user game_user_pkey; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_user
    ADD CONSTRAINT game_user_pkey PRIMARY KEY (id);


--
-- Name: game_user game_user_room_id_device_id_2c7b406d_uniq; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_user
    ADD CONSTRAINT game_user_room_id_device_id_2c7b406d_uniq UNIQUE (room_id, device_id);


--
-- Name: game_user game_user_room_id_player_id_b5fb9339_uniq; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_user
    ADD CONSTRAINT game_user_room_id_player_id_b5fb9339_uniq UNIQUE (room_id, player_id);


--
-- Name: game_user game_user_room_id_pseudo_b364005b_uniq; Type: CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.game_user
    ADD CONSTRAINT game_user_room_id_pseudo_b364005b_uniq UNIQUE (room_id, pseudo);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: dasein
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk; Type: FK CONSTRAINT; Schema: public; Owner: dasein
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

