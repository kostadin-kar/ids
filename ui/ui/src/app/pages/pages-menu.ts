import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'Home',
    icon: 'home-outline',
    link: '/pages/main',
    home: true
  },
  {
    title: 'SERVICES',
    group: true,
  },
  {
    title: 'Story service',
    icon: 'people-outline',
    link: '/pages/story'
  },
  {
    title: 'Intrusion detection system',
    icon: 'map-outline',
    link: '/pages/ids'
  },
  {
    title: 'Intruder service',
    icon: 'shield-off-outline',
    link: '/pages/intruder'
  }
];
