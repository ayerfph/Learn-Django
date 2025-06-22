# Profile Cards & Profile List (TypeScript)

A simple TypeScript/React project for displaying user profile cards and a profile list. This project demonstrates how to create reusable profile card components and render a list of user profiles with TypeScript for type safety.

## Features

- 🧑‍💼 **Profile Card**: Displays user photo, name, email, and other details.
- 📋 **Profile List**: Renders a list of profile cards from user data.
- ⚡ **TypeScript**: All components and data are strongly typed.
- 🎨 **Customizable**: Easily style and extend the components.

## Demo

![Sample Photo](https://github.com/user-attachments/assets/152471d5-5480-4b7e-a2d4-7823108d8d08)


## Getting Started

### Prerequisites

- Node.js (>= 16)
- npm or yarn

### Installation

```sh
git clone https://github.com/your-username/profile-cards-ts.git
cd profile-cards-ts
npm install
```

### Running the App

```sh
npm run dev

Open http://localhost:5173 to view it in your browser.

```


## Usage

### ProfileCard Component

```sh
// src/components/ProfileCard.tsx
import React from 'react';

export interface Profile {
  id: number;
  name: string;
  email: string;
  avatarUrl: string;
  role?: string;
}

export const ProfileCard: React.FC<{ profile: Profile }> = ({ profile }) => (
  <div className="profile-card">
    <img src={profile.avatarUrl} alt={profile.name} />
    <h2>{profile.name}</h2>
    <p>{profile.email}</p>
    {profile.role && <span>{profile.role}</span>}
  </div>
);
```

### ProfileList Component

```sh
// src/components/ProfileList.tsx
import React from 'react';
import { ProfileCard, Profile } from './ProfileCard';

const profiles: Profile[] = [
  {
    id: 1,
    name: 'Jane Doe',
    email: 'jane@example.com',
    avatarUrl: '/avatars/jane.png',
    role: 'Developer',
  },
  // Add more profiles...
];

export const ProfileList: React.FC = () => (
  <div className="profile-list">
    {profiles.map(profile => (
      <ProfileCard key={profile.id} profile={profile} />
    ))}
  </div>
);

```

### Folder Structure

```sh
src/
  components/
    ProfileCard.tsx
    ProfileList.tsx
  App.tsx
  main.tsx
public/
  avatars/
    jane.png
    ...
```

