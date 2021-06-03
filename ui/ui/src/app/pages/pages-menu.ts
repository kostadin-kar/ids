import { NbMenuItem } from '@nebular/theme';

export const MENU_ITEMS: NbMenuItem[] = [
  {
    title: 'Home',
    icon: 'home-outline',
    link: 'main'
  },
  {
    title: 'SERVICES',
    group: true,
  },
  {
    title: 'Story service',
    icon: 'people-outline',
    link: '/pages/layout/story'
  },
  {
    title: 'Intrusion detection system',
    icon: 'map-outline',
    link: '/pages/layout/ids'
  },
  {
    title: 'Intruder service',
    icon: 'shield-off-outline',
    link: '/pages/layout/intruder'
  }
];
